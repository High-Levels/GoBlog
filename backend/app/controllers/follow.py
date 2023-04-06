from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request,jsonify
from json_checker import Checker
from app import responseHandler,requestMapping,requestStruct,db,email_regex,mail
import os,hashlib
import uuid
from werkzeug.utils import secure_filename
from pony.orm import select
from app.models.follow import Follow
from app.models.user import User
from datetime import date,datetime

@jwt_required()
def follow(targetIdUser):
    response = {
        "targetUserExist": None,
        "alreadyFollowedBefore":None,
        "error": False,
        "logMsg": ""
    }
    try:
        currentUser = get_jwt_identity()
        selectTargetIdUser = select(u for u in User if u.idUser == uuid.UUID(targetIdUser))
        if len(selectTargetIdUser) == 0:
            response["targetUserExist"] = False
            response["logMsg"] = "Target user does not exist"
            return responseHandler.ok(response)
        response["targetUserExist"] = True
        selectFollowCurrentUserTargetUser = select(fol for fol in Follow 
                                                    if fol.source.idUser == uuid.UUID(currentUser["idUser"]) and 
                                                    fol.target.idUser == uuid.UUID(targetIdUser))
        if len(selectFollowCurrentUserTargetUser) != 0:
            response["alreadyFollowedBefore"] = True
            response["logMsg"] = "You already followed this user before"
            return responseHandler.ok(response)
        response["alreadyFollowedBefore"] = False
        followObject = Follow(source=currentUser["idUser"], target=targetIdUser, dateFollow = datetime.now())
        response["logMsg"] = "You now followed this user"
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        print(e)
        return responseHandler.badRequest(response)

@jwt_required()
def unfollow(targetIdUser):
    response = {
        "targetIdUserExist":None,
        "youFollowedThisUserBefore":None,
        "error":False,
        "logMsg":""
    }
    try:
        currentUser = get_jwt_identity()
        selectTargetUser = select(u for u in User if u.idUser == uuid.UUID(targetIdUser))
        if len(selectTargetUser) == 0:
            response["targetIdUserExist"] = False
            response["logMsg"] = "Target user does not exist"
            return responseHandler.ok(response)
        response["targetIdUserExist"] = True
        selectUserFollowTargetUser = select(fol for fol in Follow 
                                            if fol.source.idUser == uuid.UUID(currentUser["idUser"]) and
                                            fol.target.idUser == uuid.UUID(targetIdUser))
        if len(selectUserFollowTargetUser) == 0:
            response["youFollowedThisUserBefore"] = False
            response["logMsg"] = "You did not follow this user"
            return responseHandler.ok(response)
        response["youFollowedThisUserBefore"] = True
        selectUserFollowTargetUser.delete(bulk=True)
        response["logMsg"] = "You have unfollowed this user"
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        print(e)
        return responseHandler.badGateway(response)