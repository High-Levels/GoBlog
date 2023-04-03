from flask import Flask
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request,redirect,url_for
from json_checker import Checker
import uuid
from pony.orm import select,desc
from app.models.friend import Friend
from app.models.friendRequest import FriendRequest
from app.models.user import User
from app import requestMapping,requestStruct,responseHandler
from datetime import datetime

@jwt_required()
def getUserOutgoingFriendRequest():
    response = {
        "friendRequestList": [],
        "error":False,
        "logMsg": ""
    }
    try:
        currentUser = get_jwt_identity()
        requestJson = request.json
        for key in requestStruct.getUserFriendRequest():
            if key not in requestJson:
                response["error"] = True
                response["logMsg"] = f"Key \"{key}\" is not in request form"
            elif requestJson[key] == "":
                response["error"] = True
                response["logMsg"] = f"Request form key \"{key}\" value is blank"
        requestJsonDict = requestMapping.getUserFriendRequest(requestJson)
        requestJsonVerified = Checker(requestStruct.getUserFriendRequest(),soft=True).validate(requestJsonDict)
        maxFriendRequestPerPage = requestJsonVerified["maxFriendRequestPerPage"]
        page = requestJsonVerified["page"]
        maxFriendRequestPerPage = int(maxFriendRequestPerPage)
        page = int(page)
        if page <= 0:
            response["error"] = True
            response["logMsg"] = "Page must be higher or equal to 1"
            return responseHandler.badRequest(response)
        selectUserFriendRequestOffset = maxFriendRequestPerPage*(page-1)
        selectUserFriendRequestMax = selectUserFriendRequestOffset + maxFriendRequestPerPage
        selectUserFriendRequest = select(
            fr for fr in FriendRequest if fr.sender.idUser == uuid.UUID(currentUser["idUser"])
            ).order_by(desc(FriendRequest.dateFriendRequest))[selectUserFriendRequestOffset:selectUserFriendRequestMax]
        for fr in selectUserFriendRequest:
            response["friendRequestList"].append(
                {
                    "sender": str(fr.sender.idUser), 
                    "recipient": str(fr.recipient.idUser), 
                    "dateFriendRequest": fr.dateFriendRequest
                }
                )
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        print(e)
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
        requestJson = request.json
        print(requestJson)
        for key in requestStruct.getUserFriend():
            if key not in requestJson:
                response["error"] = True
                response["logMsg"] = f"Key \"{key}\" is not in request form"
                return responseHandler.badRequest(response)
            elif requestJson[key] == "":
                response["error"] = True
                response["logMsg"] = f"Request form key \"{key}\" value is blank"
                return responseHandler.badRequest(response)
        requestJsonDict = requestMapping.getUserFriend(requestJson)
        requestJsonVerified = Checker(requestStruct.getUserFriend(),soft=True).validate(requestJsonDict)
        maxFriendPerPage = requestJsonVerified["maxFriendPerPage"]
        page = requestJsonVerified["page"]
        maxFriendPerPage = int(maxFriendPerPage)
        page = int(page)
        if page <= 0:
            response["error"] = True
            response["logMsg"] = "Page must be higher or equal to 1"
            return responseHandler.badRequest(response)
        selectUserFriendOffset = maxFriendPerPage*(page-1)
        selectUserFriendMax = selectUserFriendOffset + maxFriendPerPage
        selectUserFriend = select(
            f for f in Friend 
            if f.userOne.idUser == uuid.UUID(currentUser["idUser"]) or f.userTwo.idUser == uuid.UUID(currentUser["idUser"])
            ).order_by(desc(Friend.dateFriend))[selectUserFriendOffset:selectUserFriendMax]
        for f in selectUserFriend:
            if f.userOne.idUser == uuid.UUID(currentUser["idUser"]):
                response["friendList"].append(
                    {
                        "otherUser": str(f.userTwo.idUser)
                    }
                    )
            elif f.userTwo.idUser == uuid.UUID(currentUser["idUser"]):
                response["friendList"].append(
                    {
                        "otherUser": str(f.userOne.idUser)
                    }
                    )
            else:
                response["error"] = True
                response["logMsg"] = "Unknown user detected. Please contact administrator to solve this problem."
                return responseHandler.badGateway(response)
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        print(e)
        return responseHandler.badGateway(response)



@jwt_required()
def sendFriendRequest(targetIdUser):
        # targetIdUserExist: does target user exist?
        # targetUserSendYouFriendRequest: does target user already send you friend request?
        # youAlreadySendFriendRequestBefore: have you sent friend request to target user before?
        # if target user already send you friend request, then automatically become friend
        response = {
            "targetIdUserExist":None,
            "alreadyFriend":None,
            "targetUserSendYouFriendRequest":None,
            "youAlreadySendFriendRequestBefore":None,
            "error":False,
            "logMsg":""
        }
        try:
            currentUser = get_jwt_identity()
            selectTargetUser = select(
            u for u in User if u.idUser == uuid.UUID(targetIdUser)
            )
            if len(selectTargetUser) == 0:
                response["error"] = True
                response["logMsg"] = "Target user does not exist"
            response["targetIdUserExist"] = True
            selectFriendWithTargetUser = select(
            f for f in Friend if 
            (f.userOne.idUser == uuid.UUID(currentUser["idUser"]) and f.userTwo.idUser == uuid.UUID(targetIdUser))
            or 
            (f.userOne.idUser == uuid.UUID(targetIdUser) and f.userTwo.idUser == uuid.UUID(currentUser["idUser"])))
            if len(selectFriendWithTargetUser) != 0:
                response["alreadyFriend"] = True
                response["logMsg"] = "You are already friend with target user"
                return responseHandler.ok(response)
            response["alreadyFriend"] = False
            selectTargetUserFriendRequest = select(
                fr for fr in FriendRequest 
                if fr.sender.idUser == uuid.UUID(targetIdUser) and fr.recipient.idUser == uuid.UUID(currentUser["idUser"]))
            if len(selectTargetUserFriendRequest) == 0:
                response["targetUserSendYouFriendRequest"] = False
                selectCurrentUserFriendRequest = select(
                    fr for fr in FriendRequest 
                    if fr.sender.idUser == uuid.UUID(currentUser["idUser"]) and fr.recipient.idUser == uuid.UUID(targetIdUser)
                )
                if len(selectCurrentUserFriendRequest) != 0:
                    response["youAlreadySendFriendRequestBefore"] = True
                else:
                    response["youAlreadySendFriendRequestBefore"] = False
                # refresh friend request
                selectCurrentUserFriendRequest.delete(bulk=True)
                FriendRequestObject = FriendRequest(
                    sender=currentUser["idUser"], recipient=targetIdUser, dateFriendRequest=datetime.now())
                response["logMsg"] = "Friend request sent."
                return responseHandler.ok(response)
            else:
                # automatically become friend
                response["targetUserSendYouFriendRequest"] = True
                selectCurrentUserFriendRequest = select(
                    fr for fr in FriendRequest 
                    if fr.sender.idUser == uuid.UUID(currentUser["idUser"]) and fr.recipient.idUser == uuid.UUID(targetIdUser)
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
            print(e)
            return responseHandler.badGateway(response)
        


@jwt_required()
def acceptFriendRequest(targetIdUser):
    # targetIdUserExist: does target id user exist?
    # friendRequestExist: does friend request exist ?
    # alreadyFriend: is target user already your friend?
    # error: does the script encountered error? 
    # logMsg: additional msg, can be used to print log or to print error when error occured
    response = {
            "targetIdUserExist":None,
            "alreadyFriend":None,
            "friendRequestExist":None,
            "error":False,
            "logMsg":""
        }
    try:
        currentUser = get_jwt_identity()
        if targetIdUser == currentUser["idUser"]:
            response["error"] = True
            response["logMsg"] = "You cannot accept friend request from yourself"
            return responseHandler.badRequest(response)
        selectTargetUser = select(
            u for u in User if u.idUser == uuid.UUID(targetIdUser)
        )
        if len(selectTargetUser) == 0:
            response["error"] = True
            response["logMsg"] = "Target user does not exist"
            return responseHandler.badGateway(response)
        response["targetIdUserExist"] = True
        selectFriendWithTargetUser = select(
            f for f in Friend if 
            (f.userOne.idUser == uuid.UUID(currentUser["idUser"]) and f.userTwo.idUser == uuid.UUID(targetIdUser))
            or 
            (f.userOne.idUser == uuid.UUID(targetIdUser) and f.userTwo.idUser == uuid.UUID(currentUser["idUser"])))
        if len(selectFriendWithTargetUser) != 0:
            response["alreadyFriend"] = True
            response["logMsg"] = "You are already friend with target user"
            return responseHandler.ok(response)
        response["alreadyFriend"] = False
        selectTargetUserFriendRequest = select(
            fr for fr in FriendRequest 
            if fr.sender.idUser == uuid.UUID(targetIdUser) and fr.recipient.idUser == uuid.UUID(currentUser["idUser"])
        )
        if len(selectTargetUserFriendRequest) == 0:
            response["error"] = True
            response["logMsg"] = "The target user have not send you friend request"
            return responseHandler.badGateway(response)
        response["friendRequestExist"] = True
        selectCurrentUserFriendRequest = select(
            fr for fr in FriendRequest 
            if fr.sender.idUser == uuid.UUID(currentUser["idUser"]) and fr.recipient.idUser == uuid.UUID(targetIdUser)
        )
        selectTargetUserFriendRequest.delete(bulk=True)
        selectCurrentUserFriendRequest.delete(bulk=True)
        FriendObject = Friend(userOne=currentUser["idUser"], userTwo=targetIdUser, dateFriend=datetime.now())
        response["logMsg"] = "Friend request accepted"
        return responseHandler.ok(response)
    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        print(e)
        return responseHandler.badGateway(response)
    
    
    
     
