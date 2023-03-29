from app.models import db
from app import requestMapping,requestStruct,responseHandler
from flask import request,jsonify
from json_checker import Checker
from uuid import uuid4
from flask_jwt_extended import get_jwt_identity,jwt_required
from pony.orm import select,exists
from app.models.category import Category

def listCategory():
    try:
        listCategory = select(a for a in Category)[:]
        data = []
        for i in range(len(listCategory)):
            data.append(listCategory[i].to_dict())
        #print(data[0]['idCategory'])
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
            data = requestMapping.Category(request.json)
            result = Checker(requestStruct.Category(),soft=True).validate(data)
            checkCategory = Category.get(name = result['name'])
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
                #Create
                Category(idCategory = str(uuid4()) ,name = result['name'])
                response = {
                    "Data": result,
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
        readById = Category.get(idCategory = id)
        data = readById.to_dict()
        response = {
            "Data": data
        }
        return responseHandler.ok(response)
    except Exception as err:
        response = {
            "Message": "No Data Found"
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
            checkName = db.select(f"select name from tbl_category where name = '{result['name']}' and name != (select name from tbl_category where id_category = '{id}')")
            if checkName:
                response = {
                    "Message": "Category is Exist"
                }
                return responseHandler.badRequest(response)
            #Update
            Category[id].set(**result)
            response = {
                "Data": result,
                "Message": "Success Update Category"
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
            selectById = Category.get(idCategory = id)
            if not selectById:
                response = {
                    "Message": "Data Not Found"
                }
                return responseHandler.badRequest(response)
            elif selectById:
                Category[id].delete()
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
