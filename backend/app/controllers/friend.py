from flask import Flask
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request,redirect,url_for
from json_checker import Checker
from uuid import uuid4
from pony.orm import select,desc
from app.models.friend import Friend
from app.models.friendRequest import FriendRequest
from app.models.user import User
from app import requestMapping,requestStruct,responseHandler
from datetime import datetime

@jwt_required()
def getUserFriendRequest():
    response = {
        "friendRequestList": [],
        "error":False,
        "logMsg": ""
    }
    try:
        currentUser = get_jwt_identity()
        requestForm = request.form
        for key in requestStruct.getUserFriendRequest():
            if key not in requestForm:
                response["error"] = True
                response["logMsg"] = f"Key \"{key}\" is not in request form"
            elif requestForm[key].strip() == "":
                response["error"] = True
                response["logMsg"] = f"Request form key \"{key}\" value is blank"
        requestFormDict = requestMapping.getUserFriendRequest(requestForm)
        requestFormVerified = Checker(requestFormDict,soft=True).validate(requestStruct.getUserFriendRequest)
        maxFriendRequestPerPage = requestFormVerified["maxFriendRequestPerPage"]
        page = requestFormVerified["page"]
        maxFriendRequestPerPage = int(maxFriendRequestPerPage)
        page = int(page)
        if page <= 0:
            response["error"] = True
            response["logMsg"] = "Page must be higher or equal to 1"
            return responseHandler.badRequest(response)
        selectUserFriendRequestOffset = maxFriendRequestPerPage*(page-1)
        selectUserFriendRequestMax = selectUserFriendRequestOffset + maxFriendRequestPerPage
        selectUserFriendRequest = select(
            fr for fr in FriendRequest if fr.sender == currentUser["idUser"]
            ).order_by(desc(FriendRequest.dateFriendRequest))[selectUserFriendRequestOffset:selectUserFriendRequestMax]
        for fr in selectUserFriendRequest:
            response["friendRequestList"].append(
                [fr.sender, fr.recipient, fr.dateFriendRequest]
                )
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        return responseHandler.badGateway(response)

@jwt_required()
def getUserFriend():
    response = {
        "friendList": [],
        "error":False,
        "logMsg": ""
    }
    try:
        currentUser = get_jwt_identity()
        requestForm = request.form
        for key in requestStruct.getUserFriend():
            if key not in requestForm:
                response["error"] = True
                response["logMsg"] = f"Key \"{key}\" is not in request form"
            elif requestForm[key].strip() == "":
                response["error"] = True
                response["logMsg"] = f"Request form key \"{key}\" value is blank"
        requestFormDict = requestMapping.getUserFriend(requestForm)
        requestFormVerified = Checker(requestFormDict,soft=True).validate(requestStruct.getUserFriend)
        maxFriendPerPage = requestFormVerified["maxFriendPerPage"]
        page = requestFormVerified["page"]
        maxFriendPerPage = int(maxFriendPerPage)
        page = int(page)
        if page <= 0:
            response["error"] = True
            response["logMsg"] = "Page must be higher or equal to 1"
            return responseHandler.badRequest(response)
        selectUserFriendOffset = maxFriendPerPage*(page-1)
        selectUserFriendMax = selectUserFriendOffset + maxFriendPerPage
        selectUserFriend = select(
            f for f in Friend if f.userOne == currentUser["idUser"] or f.userTwo == currentUser["idUser"]
            ).order_by(desc(Friend.dateFriend))[selectUserFriendOffset:selectUserFriendMax]
        for f in selectUserFriend:
            response["friendList"].append(
                [f.sender, f.recipient, f.dateFriendRequest]
                )
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        return responseHandler.badGateway(response)



@jwt_required()
def sendFriendRequest(targetIdUser):
        # targetIdUserExist: does target user exist?
        # targetUserSendYouFriendRequest: does target user already send you friend request?
        # youAlreadySendFriendRequestBefore: have you sent friend request to target user before?
        # if target user already send you friend request, then automatically become friend
        response = {
            "targetIdUserExist":None,
            "targetUserSendYouFriendRequest":None,
            "youAlreadySendFriendRequestBefore":None,
            "error":False,
            "logMsg":""
        }
        try:
            currentUser = get_jwt_identity()
            selectTargetUser = select(
            u for u in User if u.idUser == targetIdUser
            )
            if len(selectTargetUser) == 0:
                response["error"] = True
                response["logMsg"] = "Target user does not exist"
            response["targetIdUserExist"] = True
            selectTargetUserFriendRequest = select(
                fr for fr in FriendRequest if fr.sender == targetIdUser and fr.recipient == currentUser["idUser"])
            if len(selectTargetUserFriendRequest) == 0:
                response["targetUserSendYouFriendRequest"] = False
                selectCurrentUserFriendRequest = select(
                    fr for fr in FriendRequest if fr.sender == currentUser["idUser"] and fr.recipient == targetIdUser
                )
                if len(selectCurrentUserFriendRequest) != 0:
                    response["youAlreadySendFriendRequestBefore"] = True
                else:
                    response["youAlreadySendFriendRequestBefore"] = False
                # refresh friend request
                selectCurrentUserFriendRequest.delete(bulk=True)
                FriendRequestObject = FriendRequest(
                    sender=currentUser["idUser"], recipient=targetIdUser, dateFriendRequest=datetime.now())
                return responseHandler.ok(response)
            else:
                # automatically become friend
                response["targetUserSendYouFriendRequest"] = True
                selectCurrentUserFriendRequest = select(
                    fr for fr in FriendRequest if fr.sender == currentUser["idUser"] and fr.recipient == targetIdUser
                )
                if len(selectCurrentUserFriendRequest) != 0:
                    response["youAlreadySendFriendRequestBefore"] = True
                else:
                    response["youAlreadySendFriendRequestBefore"] = False
                selectTargetUserFriendRequest.delete(bulk=True)
                selectCurrentUserFriendRequest.delete(bulk=True)
                FriendObject = Friend(userOne=currentUser["idUser"], userTwo=targetIdUser, dateFriend=datetime.now())
                response["logMsg"] = "Target user already sent you friend request. You are now friend with target user."
                return responseHandler.ok(response)
        except Exception as e:
            response["error"] = True
            response["logMsg"] = str(e)
            return responseHandler.badGateway(response)
        


@jwt_required()
def acceptFriendRequest(targetIdUser):
    # targetIdUserExist: does target id user exist?
    # friendRequestExist: does friend request exist ?
    # error: does the script encountered error? 
    # logMsg: additional msg, can be used to print log or to print error when error occured
    response = {
            "targetIdUserExist":None,
            "friendRequestExist":None,
            "error":False,
            "logMsg":""
        }
    try:
        currentUser = get_jwt_identity()
        selectTargetUser = select(
            u for u in User if u.idUser == targetIdUser
        )
        if len(selectTargetUser) == 0:
            response["error"] = True
            response["logMsg"] = "Target user does not exist"
            return responseHandler.badGateway(response)
        response["targetIdUserExist"] = True
        selectTargetUserFriendRequest = select(
            fr for fr in FriendRequest if fr.sender == targetIdUser and fr.recipient == currentUser["idUser"]
        )
        if len(selectTargetUserFriendRequest) == 0:
            response["error"] = True
            response["logMsg"] = "The target user have not send you friend request"
            return responseHandler.badGateway(response)
        response["friendRequestExist"] = True
        selectCurrentUserFriendRequest = select(
            fr for fr in FriendRequest if fr.sender == currentUser["idUser"] and fr.recipient == targetIdUser
        )
        selectTargetUserFriendRequest.delete(bulk=True)
        selectCurrentUserFriendRequest.delete(bulk=True)
        FriendObject = Friend(userOne=currentUser["idUser"], userTwo=targetIdUser, dateFriend=datetime.now())
        response["logMsg"] = "Friend request accepted"
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        return responseHandler.badGateway(response)
    
    
    
     
