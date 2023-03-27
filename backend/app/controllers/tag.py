from app.models import db
from app import requestMapping,requestStruct,responseHandler
from flask import request
from json_checker import Checker
from uuid import uuid4
from flask_jwt_extended import get_jwt_identity,jwt_required

def listTag():
    try:
        listTag = db.select(f"select id_tag, name from tbl_tag")
        data = []
        for i in listTag:
            data.append({
                "id": i[0],
                "tag": i[1]
            })
        return responseHandler.ok(data)
    except Exception as err:
        response = {
            "Message": str(err)
        }
        return responseHandler.badGateway(response)
    
@jwt_required()
def createTag():
    currentUser = get_jwt_identity()
    try:
        if currentUser:
            jsonBody = request.json
            data = requestMapping.Tag(jsonBody)
            result = Checker(requestStruct.Tag(),soft=True).validate(data)
            checkTag = db.select(f"select *from tbl_tag where name = '{result['name']}'")
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
                createTag = (f"insert into tbl_tag(id_tag,name) values ('{str(uuid4())}','{result['name']}')")
                db.execute(createTag)
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
