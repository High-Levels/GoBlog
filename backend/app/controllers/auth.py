from app.models import db
from app import responseHandler
from flask import jsonify,request
import flask
import hashlib,os
from flask_jwt_extended import create_refresh_token,create_access_token,set_access_cookies,get_jwt_identity,jwt_required,unset_jwt_cookies,unset_access_cookies,set_refresh_cookies,unset_refresh_cookies

def login():
    try:
        jsonBody = request.json
        hashpassword = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select id_user,username from tbl_user where username = '{jsonBody['username']}' and password = '{hashpassword.hexdigest()}' ")
        for i in user:
            userAuth = {
                "idUser": i[0],
                "username": i[1]
            }
        if user:
            accessToken = create_access_token(identity=userAuth,fresh=True)
            refreshToken = create_refresh_token(identity=userAuth)
            response = jsonify({
                "accessToken": accessToken,
                "Message": "Login Success"})
            set_refresh_cookies(response, refreshToken)
            set_access_cookies(response, accessToken)
            return response
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
