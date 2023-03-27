from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from json_checker import Checker
from app import responseHandler,requestMapping,requestStruct,db,email_regex,allowedextensions,uploadFolderUsers
import os,hashlib
from uuid import uuid4
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowedextensions

def createUser():
    try:
        jsonBody = request.json
        data = requestMapping.createUser(jsonBody)
        result = Checker(requestStruct.User(),soft = True).validate(data)
        checkUser = db.select(f"select *from tbl_user where username = '{jsonBody['username']}' or email = '{jsonBody['email']}'")

        if jsonBody['username']=="" or jsonBody['email']==""or jsonBody['password']=="":
            response = {
                    "Message": "All Data Must be Filled"
                }
            return responseHandler.badRequest(response)
        if checkUser:
                response = {
                    "Message": (f"Username or Email is Exist")
                }
                return responseHandler.badRequest(response)
        elif email_regex.match(result['email']):
            password = result['password']
            hashpassword = hashlib.md5((password+ os.getenv("SALT_PASSWORD")).encode())
            createUser = (f"insert into tbl_user(id_user,username,email,password,date_register) values('{str(uuid4())}','{result['username']}','{result['email']}','{hashpassword.hexdigest()}',now())")
            db.execute(createUser)
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
    
@jwt_required(fresh=True)
def readUser(id=None):
    currentUser = get_jwt_identity()
    if id is None:
        id = currentUser['idUser']
    if currentUser['idUser'] == id:
        try:
            readById = db.select(f"select id_user,username,email,password,name,gender,address,birth,phone_number,date_register,picture from tbl_user where id_user = '{id}'" )
            data = []
            for i in readById:
                data.append({
                    "idUser": i[0],
                    "username":i[1],
                    "email": i[2],
                    "password": i[3],
                    "name": i[4],
                    "gender": i[5],
                    "address": i[6],
                    "birth": i[7],
                    "phoneNumber":i[8],
                    "dateRegister":i[9],
                    "picture":i[10]
                })
            if not data:
                    response = {
                        "Message": "User Not Found"
                    }
                    return responseHandler.badRequest(response)
            response ={
                    "Data": data[0]
                }
            return responseHandler.ok(response)
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
def updateUser(id):
    currentUser = get_jwt_identity()
    if currentUser['idUser'] == id:
        jsonBody = request.form
        files = request.files.getlist('picture')
        data = requestMapping.userUpdate(jsonBody)
        result = Checker(requestStruct.userUpdate(),soft=True).validate(data)
        hashpass = hashlib.md5((result['password']+os.getenv("SALT_PASSWORD")).encode())
        success = False
        try:
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
                for user in db.select(f"select id_user,picture from tbl_user where id_user = '{currentUser['idUser']}'"): 
                    user = {
                        "id_user": user[0],
                        "pic_user": user[1]
                    } 
                for i in files:
                    if i and allowed_file(i.filename):
                        try:
                            os.remove(os.path.join(uploadFolderUsers, user['pic_user']))
                        except:
                            pass
                        filename = secure_filename(i.filename)
                        picfilename = currentUser['idUser'] + '_' + filename
                        i.save(os.path.join(uploadFolderUsers,picfilename))
                        success = True
                    if success:
                        updateUser = (f"update tbl_user set username='{result['username']}' ,password = '{hashpass.hexdigest()}',email='{result['email']}',name='{result['name']}',gender='{result['gender']}',address='{result['address']}',birth='{result['birth']}',phone_number='{result['phoneNumber']}',picture = '{picfilename}' where id_user = '{currentUser['idUser']}'")
                        db.execute(updateUser)
                        response = {
                            "Data": updateUser,
                            "Message": "Success Update User"
                        }
                        return responseHandler.ok(response)
                    elif not success:
                        response = { 
                            "Message": "File is not Valid"
                        }
                        return responseHandler.badRequest(response)
                if not files:
                    updateUser = (f"update tbl_user set username='{result['username']}' ,password = '{hashpass.hexdigest()}',email='{result['email']}',name='{result['name']}',gender='{result['gender']}',address='{result['address']}',birth='{result['birth']}',phone_number='{result['phoneNumber']}' where id_user = '{currentUser['idUser']}'")
                    db.execute(updateUser)
                    response = {
                        "Data": updateUser,
                        "Message": "Success Update User"
                    }
                    return responseHandler.ok(response)
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
            selectById = (f"select id_user from tbl_user where id_user = '{id}'")
            data = []
            for i in db.execute(selectById):
                data.append({
                    "idUser": i[0]
                })
            if not data:
                response = {
                    "Message": "Data Not Found"
                }
                return responseHandler.badRequest(response)
            elif data:
                deleteById = (f"delete from tbl_user where id_user = '{id}'")
                db.execute(deleteById)
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
    
     


