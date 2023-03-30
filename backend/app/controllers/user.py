from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request,jsonify
from json_checker import Checker
from app import responseHandler,requestMapping,requestStruct,db,email_regex,mail
import os,hashlib
from uuid import uuid4
from werkzeug.utils import secure_filename
from pony.orm import select
from app.models.user import User
from datetime import date,datetime
from cloudinary.uploader import upload
import cloudinary
from flask_mail import Message


def sendEmail(email,id):
    sendMail = Message(
                 subject = "Activate Your Account",
                 sender = 'upgradelvel@gmail.com',
                 recipients = [email],
                 body= f"Activate Your Account here : http://127.0.0.1:5000/activate/{id}"
            )
    return sendMail


def createUser():
    try:
        jsonBody = request.json
        data = requestMapping.createUser(jsonBody)
        result = Checker(requestStruct.User(),soft = True).validate(data)
        checkUser = select(a for a in User if a.username is result['username'] or a.email is result['email'])[:]
        if result['username']=="" or result['email']==""or result['password']=="":
            response = {
                    "Message": "All Data Must be Filled"
                }
            return responseHandler.badRequest(response)
        if checkUser:
                response = {
                    "Message": "Username or Email is Exist"
                }
                return responseHandler.badRequest(response)
        elif email_regex.match(result['email']):
            hashpassword = (hashlib.md5((result['password']+ os.getenv("SALT_PASSWORD")).encode())).hexdigest()
            #CREATE
            idUser = str(uuid4())
            User(idUser = idUser,username = result['username'],email = result['email'], password = hashpassword,dateRegister = datetime.now(), isActivated = False)
            sendMail = sendEmail(result['email'],idUser)
            mail.send(sendMail)
            response = {
                    "Data": jsonBody,
                    "Message": "Data Created"
                }
            return responseHandler.ok(response)
        else:
            response = {
                    "Message": "Email not Valid"
                }
            return responseHandler.badRequest(response)

    except Exception as err:
        response ={
                "Error": str(err)
            }
        return responseHandler.badGateway(response)

def activateUser(id):
    try:
        User[id].set(isActivated = True)
        response = {
            "Message": "Account is Activated"
        }
        return responseHandler.ok(response)
    except Exception as err:
        response = {
            "Error": str(err)
        }
        return responseHandler.badGateway(response)
    
@jwt_required()
def readUser(id):                     
    try:
        readById = User.get(idUser = id)
        data = readById.to_dict()
    
        response = {
            "Data": data
        } 
        return responseHandler.ok(response)
    except Exception as err:
            response = {
                "Message": "User Not Found"
            }
            return responseHandler.badRequest(response)
    
@jwt_required()
def updateUser(id):
    currentUser = get_jwt_identity()
    if currentUser['idUser'] == id:
        uploadFile = request.files['picture']
        data = requestMapping.userUpdate(request.form)
        result = Checker(requestStruct.userUpdate(),soft=True).validate(data)
        hashpass = (hashlib.md5((result['password']+os.getenv("SALT_PASSWORD")).encode())).hexdigest()
        success = False
        try:
            # a = select(a for a in User if str(a.idUser) is currentUser['idUser'])[:]
            # print(a[0].idUser)
            # check = User.get(username = result['username'] and select(), email = result['email'] and select(a for a in User if str(a.idUser) != currentUser['idUser']))
            # print(check)
            checkUsername = db.select(f"select username from tbl_user where username = '{result['username']}' and username != (select username from tbl_user where id_user = '{currentUser['idUser']}')")
            checkEmail = db.select(f"select email from tbl_user where email = '{result['email']}' and email != (select email from tbl_user where id_user = '{currentUser['idUser']}')")
            if checkUsername:
                response = {
                    "Message": "User is exist"
                }
                return responseHandler.badRequest(response)
            elif checkEmail:
                response = {
                    "Message": "Email is exist"
                }
                return responseHandler.badRequest(response)
            if result['username'] =="" or result['email'] =="" or result['password'] =="" or result['name'] =="" or result['gender'] =="" or result['address'] == "" or result['birth'] =="" or result['phoneNumber'] =="":
                response = {
                    "Message": "All Data Must be Filled"
                }
                return responseHandler.badRequest(response)
            if email_regex.match(result['email']):
                #user = select(a for a in User if str(a.idUser) is currentUser['idUser'])[:]
                cloudinary.uploader.upload(uploadFile,
                                               folder = "profiles/",
                                               public_id = "profile"+"_"+currentUser['idUser'],
                                               overwrite = True,
                                               width = 250,
                                               height = 250,
                                               grafity = "auto",
                                               radius = "max",
                                               crop = "fill"
                                               )
                success = True
                if success:
                        result = Checker(requestStruct.userUpdate(),soft=True).validate(data)
                        User[id].set(username = result['username'],email = result['email'], password = hashpass, name = result['name'], gender = result['gender'], address = result['address'], birth = result['birth'],phoneNumber = result['phoneNumber'],picture = "profile"+"_"+currentUser['idUser'])
                        response = {
                            "Data": result,
                            "Message": "Success Update User"
                        }
                        return responseHandler.ok(response)
                elif not success:
                        response = { 
                            "Message": "File is not Valid"
                        }
                        return responseHandler.badRequest(response)
            response = {
                "Message": "Email not Valid"
            }
            return responseHandler.badRequest(response)
        except Exception as err:
            response = {
                "Error": str(err)
            }
            return responseHandler.badGateway(response)
    else:
        response = {
            "Message": "You are Not Allowed Here"
        }
        return responseHandler.badRequest(response)
    

@jwt_required(fresh=True)
def deleteUser(id):
    currentUser = get_jwt_identity()
    try:
        if currentUser['idUser'] == id:    
            selectById = User.get(idUser = id)
            if not selectById:
                response = {
                    "Message": "Data Not Found"
                }
                return responseHandler.badRequest(response)
            elif selectById:
                User[id].delete()
                response = {
                    "Message": "Delete Success"
                }
                return responseHandler.ok(response)
            response = {
                "Message": "Delete Invalid"
            }
            return responseHandler.badRequest(response)
        else:
            response = {
                "Message": "You are Not Allowed Here"
            }
            return responseHandler.badRequest(response)
    except Exception as err:
            response = {
                "Error": str(err)
            }
            return responseHandler.badGateway(response)
    
     


