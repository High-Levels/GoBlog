from app.models import db
from app import responseHandler
from flask import jsonify,request
import flask
from flask import redirect
import hashlib,os
from flask_jwt_extended import create_refresh_token,create_access_token,set_access_cookies
from flask_jwt_extended import get_jwt_identity,jwt_required,unset_jwt_cookies,unset_access_cookies
from flask_jwt_extended import set_refresh_cookies,unset_refresh_cookies
from app.models.user import User
from pony.orm import select
from flask_wtf.csrf import generate_csrf
from flask_wtf.csrf import validate_csrf
from urllib.parse import urlencode
import urllib.parse as urlparse
from requests import post
from requests import get
from uuid import uuid4
import datetime
import json
import traceback
# https://stackoverflow.com/questions/3542881/python-opposite-function-urllib-urlencode

@jwt_required(optional=True)
def googleLoginCallback():
    # https://developers.google.com/identity/openid-connect/openid-connect
    try:
        requestArgs = request.args
        requiredURLParameter = ["state", "code", "scope"]
        for urlParameter in requiredURLParameter:
            if urlParameter not in requestArgs:
                return responseHandler.badRequest("'%s\' not in url parameter" % urlParameter)
        googleTokenEndpoint = os.getenv("GOOGLE_TOKEN_ENDPOINT")
        googleLoginTokenRequest = post(googleTokenEndpoint, data={
            "code": requestArgs["code"],
            "client_id": os.getenv("GOOGLE_LOGIN_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_LOGIN_CLIENT_SECRET"),
            "redirect_uri": os.getenv("GOOGLE_LOGIN_CALLBACK_URL"),
            "grant_type": "authorization_code"
        })
        if not googleLoginTokenRequest.ok:
            return responseHandler.badGateway("Google token endpoint returned error: " 
                                              + str(json.loads(googleLoginTokenRequest.content)))
        googleLoginTokenJson = json.loads(googleLoginTokenRequest.content)
        if "error" in googleLoginTokenJson:
            return responseHandler.badGateway("Google token endpoint returned error: " + googleLoginTokenJson)
        googleLoginUserinfoRequest = get(os.getenv("GOOGLE_SCOPE_USERINFO_ENDPOINT"), params={
            "access_token": googleLoginTokenJson["access_token"]
        })
        if not googleLoginUserinfoRequest.ok:
            return responseHandler.badGateway("Google userinfo endpoint returned error: " 
                                              + str(json.loads(googleLoginUserinfoRequest.content)))
        googleLoginUserinfoJson = json.loads(googleLoginUserinfoRequest.content)
        if "error" in googleLoginUserinfoJson:
            return responseHandler.badGateway("Google userinfo endpoint returned error: " 
                                              + str(json.loads(googleLoginUserinfoRequest.content)))
        userGoogleEmail = googleLoginUserinfoJson["email"]
        userGoogleEmailVerified = googleLoginUserinfoJson["email_verified"]
        print(userGoogleEmail)
        print(userGoogleEmailVerified)
        if get_jwt_identity() == None:
            selectExistingUserByEmail = select(u for u in User if u.email == userGoogleEmail or u.googleEmail == userGoogleEmail)
            if len(selectExistingUserByEmail) != 0:
                currentUser = selectExistingUserByEmail[:][0]
                if currentUser.isActivated == False:
                    if userGoogleEmailVerified == False:
                        return responseHandler.badGateway("Your account email is not activated, please activate your email.")
                    else:
                        currentUser.isActivated = True
                if currentUser.googleEmail is None or not currentUser.googleEmail:
                    currentUser.email = userGoogleEmail
                currentUser = currentUser.to_dict()
                accessToken = create_access_token(identity=currentUser,fresh=True)
                refreshToken = create_refresh_token(identity=currentUser)
                response = {
                    "accessToken": accessToken,
                    "refreshToken": refreshToken,
                    "Message": "Login Success"}
                return responseHandler.ok(response)
            else:
                # because in login and register process the password is hashed, then
                # the password in database is stored in hashed form
                # the default password hash for google account is 0
                # this is still safe because nobody knows the input of the hash function
                # that result in 0
                currentUser = User(idUser=uuid4(), username=str(uuid4()), 
                                   email=userGoogleEmail, password="0", googleEmail=userGoogleEmail,
                                   isActivated=True, dateRegister=datetime.datetime.now()).to_dict()
                accessToken = create_access_token(identity=currentUser,fresh=True)
                refreshToken = create_refresh_token(identity=currentUser)
                response = {
                    "accessToken": accessToken,
                    "refreshToken": refreshToken,
                    "Message": "Login Success"}
                return responseHandler.ok(response)
        else:
            # If user dont have google email, then bind the email to current user
            # If user email or user account google email is equal to user google email, then login
            # Otherwise throw error asking user to unbind current google email first in order to change the account google email
            currentUser = get_jwt_identity()
            # Pony store None value as empty string
            if not currentUser["googleEmail"]:
                currentUser = select(u for u in User if u.username == currentUser["username"])[:][0]
                currentUser.googleEmail = userGoogleEmail
                currentUser = currentUser.to_dict()
                accessToken = create_access_token(identity=currentUser,fresh=True)
                refreshToken = create_refresh_token(identity=currentUser)
                response = {
                    "accessToken": accessToken,
                    "refreshToken": refreshToken,
                    "Message": "Google email binded to current account"}
                return responseHandler.ok(response)
            else:
                if currentUser["googleEmail"] == userGoogleEmail or currentUser["email"] == userGoogleEmail:
                    accessToken = create_access_token(identity=currentUser,fresh=True)
                    refreshToken = create_refresh_token(identity=currentUser)
                    response = {
                        "accessToken": accessToken,
                        "refreshToken": refreshToken,
                        "Message": "Login Success"}
                    return responseHandler.ok(response)
                else:
                    return responseHandler.badRequest("You are already logged in, but your account google email and "
                                                      "account google email does not match current google. "
                                                      "If you want to change your account google email, please unbind the "
                                                      "account google email first and then login with google again.")
    except Exception as e:
        traceback.print_exception(e)
        return responseHandler.badGateway(str(e))

def googleLoginStart():
    try:
        # https://developers.google.com/identity/openid-connect/openid-connect
        loginURLParameterDict = {
            "response_type": "code",
            "client_id": os.getenv("GOOGLE_LOGIN_CLIENT_ID"),
            "scope": "email profile",
            "redirect_uri": os.getenv("GOOGLE_LOGIN_CALLBACK_URL"),
            # state will be the parameter of the callback url,
            # it can be anything as long as encoded in url format
            # the callback url can retrieve the data with request.args.get("state")
            "state": urlencode({
                "test":123
            }),
            "access_type": "offline"        
        }
        googleLoginBaseURL = os.getenv("GOOGLE_AUTHORIZATION_ENDPOINT")
        # split url into part,
        # the url parameter is in index 4
        url_parts = list(urlparse.urlparse(googleLoginBaseURL))
        # urlparse.parse_qsl convert the url parameter into list of 2-item tuple,
        # the first item in the tuple is the key, and the second item is the value
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(loginURLParameterDict)
        # set the url parameter part with the new url parameter
        url_parts[4] = urlencode(query)
        # get the complete login url
        googleLoginURL = urlparse.urlunparse(url_parts)
        print(googleLoginURL)
        return redirect(googleLoginURL)
    except Exception as e:
        print(e)
        return responseHandler.badGateway("An error have occured")

@jwt_required(optional=True)
def login():
    try:
        currentUser = get_jwt_identity()
        if currentUser != None:
            response = {
                "Message": "You are already logged in !"
            }
            return responseHandler.badRequest(response)
        jsonBody = request.json
        hashpassword = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = select(a for a in User if a.username is jsonBody['username'] and a.password is hashpassword.hexdigest())[:]
        if not user:
            response ={
                "Message": "Username / Password is invalid"
            }
            return responseHandler.badRequest(response)
        elif user:
            currentUser = user[0].to_dict()

            #in deployment set to false only
            if currentUser['isActivated'] == False or currentUser['isActivated'] == True:
                accessToken = create_access_token(identity=currentUser,fresh=True)
                refreshToken = create_refresh_token(identity=currentUser)
                response = jsonify({
                    "accessToken": accessToken,
                    "refreshToken": refreshToken,
                    "Message": "Login Success"})
                return response
            else:
                response ={
                    "Message": "Please Activate your Email"
                }
            return responseHandler.badRequest(response)
        else:
            response ={
                "Message": "Username / Password is invalid"
            }
            return responseHandler.badRequest(response)
    except Exception as err:
        response ={
            "Error": str(err)
        }
        return responseHandler.badGateway(response)
    
@jwt_required()
def logout():
    try:
        currentUser = get_jwt_identity()
        if currentUser:
            response = {
                "Message": "Logout Successfull"
            }
            unset_access_cookies(jsonify(response))
            unset_refresh_cookies(jsonify(response))
            return responseHandler.ok(response)
        else:
            response = {
                "Message": "Logout Unccessfull"
            }
            return responseHandler.badRequest(response)
    except Exception as err:
        response = {
                "Error": str(err)
            }
        return responseHandler.badGateway(response)
