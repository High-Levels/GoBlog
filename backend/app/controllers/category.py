from app.models import db
from app import requestMapping,requestStruct,responseHandler
from flask import request
from json_checker import Checker
from uuid import uuid4
from flask_jwt_extended import get_jwt_identity,jwt_required

def listCategory():
    try:
        listCategory = db.select(f"select id_category, name from tbl_category")
        data = []
        for i in listCategory:
            data.append({
                "id": i[0],
                "category": i[1]
            })
        return responseHandler.ok(data)
    except Exception as err:
        response = {
            "Message": str(err)
        }
        return responseHandler.badGateway(response)
    
@jwt_required()
def createCategory():
    currentUser = get_jwt_identity()
    try:
        if currentUser['username'] == "Admin":
            jsonBody = request.json
            data = requestMapping.Category(jsonBody)
            result = Checker(requestStruct.Category(),soft=True).validate(data)
            checkCategory = db.select(f"select *from tbl_category where name = '{result['name']}'")
            if result['name'] == "":
                response = {
                    "Message" : "All Data Must be Filled"
                }
                return responseHandler.badRequest(response)
            if checkCategory:
                response = {
                    "Message": "Category is Exist"
                }
                return responseHandler.badRequest(response)
            else:
                createBookCategory = (f"insert into tbl_category(id_category,name) values ('{str(uuid4())}','{result['name']}')")
                db.execute(createBookCategory)
                response = {
                    "Data": jsonBody,
                    "Message": "Data Created"
                }
                return responseHandler.ok(response)
        else:
            response = {
                "Message": "You are Not Allowed Here"
            }
            return responseHandler.badRequest(response)
    except Exception as err:
            response ={
                "Error": str(err)
            }
            return responseHandler.badGateway(response)    
    
    
def readCategory(id):
    try:
        readById = db.select(f"select id_category,name from tbl_category where id_category = '{id}'")
        data = []
        for i in readById:
            data.append({
                "idCategory": i[0],
                "category": i[1]
            })
        if not data:
            response = {
                "Message": "No Data Found"
            }
            return responseHandler.badRequest(response)
        response = {
            "Data": data[0]
        }
        return responseHandler.ok(response)
    except Exception as err:
        response = {
            "Error": str(err)
        }
        return responseHandler.badGateway(response)

@jwt_required()
def updateCategory(id):
    currentUser = get_jwt_identity()
    try:
        if currentUser['username'] == "Admin":
            jsonBody = request.json
            data = requestMapping.Category(jsonBody)
            result = Checker(requestStruct.Category(),soft=True).validate(data)
            updateCategory = (f"update tbl_category set name='{result['name']}' where id_category = '{id}'")
            db.execute(updateCategory)
            response = {
                "Data": updateCategory,
                "Message": "Success Update Publisher"
            }
            return responseHandler.ok(response)
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
    
    
@jwt_required()
def deleteCategory(id):
    currentUser = get_jwt_identity()
    try:
        if currentUser['username'] == "Admin":
            selectById = (f"select id_category from tbl_category where id_category = '{id}'")
            data = []
            for i in db.execute(selectById):
                data.append({
                    "idCategory": i[0]
                })
            if not data:
                response = {
                    "Message": "Data Not Found"
                }
                return responseHandler.badRequest(response)
            elif data:
                deleteById = (f"delete from tbl_category where id_category ='{id}'")
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
