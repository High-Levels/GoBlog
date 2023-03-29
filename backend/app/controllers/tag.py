from app.models import db
from app import requestMapping,requestStruct,responseHandler
from flask import request
from json_checker import Checker
from uuid import uuid4
from flask_jwt_extended import get_jwt_identity,jwt_required
from pony.orm import select
from app.models.tag import Tag

def listTag():
    try:
        listTag = select(a for a in Tag)[:]
        data = []
        for i in range(len(listTag)):
            data.append(listTag[i].to_dict())
        return responseHandler.ok(data)
    except Exception as err:
        response = {
            "Message": str(err)
        }
        return responseHandler.badGateway(response)
    
@jwt_required()
def createTag():
    try:
            data = requestMapping.Tag(request.json)
            result = Checker(requestStruct.Tag(),soft=True).validate(data)
            checkTag = Tag.get(name = result['name'])
            if result['name'] == "":
                response = {
                    "Message" : "All Data Must be Filled"
                }
                return responseHandler.badRequest(response)
            if checkTag:
                response = {
                    "Message": "Tag is Exist"
                }
                return responseHandler.badRequest(response)
            else:
                Tag(idTag = str(uuid4()),name = result['name'])
                response = {
                    "Data": result,
                    "Message": "Data Created"
                }
                return responseHandler.ok(response)
    except Exception as err:
            response ={
                "Error": str(err)
            }
            return responseHandler.badGateway(response)    
