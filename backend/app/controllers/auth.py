from app.models import db
from app import responseHandler
from flask import jsonify,request
import flask
import hashlib,os
from flask_jwt_extended import create_refresh_token,create_access_token,set_access_cookies,get_jwt_identity,jwt_required,unset_jwt_cookies,unset_access_cookies,set_refresh_cookies,unset_refresh_cookies
from app.models.user import User
from pony.orm import select
def login():
    try:
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
