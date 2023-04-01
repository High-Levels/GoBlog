from flask import Flask
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from json_checker import Checker
from uuid import uuid4
from pony.orm import select,desc
from app.models.friend import Friend
from app.models.friend import FriendRequest
from app.models.friend import User
from app import requestMapping,requestStruct,responseHandler
from datetime import datetime

@jwt_required
def getFriendRequest():
    currentUser = get_jwt_identity()
    jsonBody = request.form
    data = requestMapping.userFriendRequest(jsonBody)
    result = Checker(requestStruct.userFriendRequest,soft=True).validate(data)
    maxFriendRequestPerPage = result["maxFriendRequestPerPage"]
    page = result["page"]
    if maxFriendRequestPerPage == "":
        maxFriendRequestPerPage = 10
    if page == "":
        page = 1
    maxFriendRequestPerPage = int(maxFriendRequestPerPage)
    page = int(page)
    if page <= 0:
        response = {
            "Data" : "Page must be >=1"
        }
        return responseHandler.badRequest(response)
    selectFriendRequestOffset = maxFriendRequestPerPage*(page-1)
    selectFriendRequestMax = selectFriendRequestOffset + maxFriendRequestPerPage
    selectFriendRequest = select(
        fr for fr in FriendRequest 
        if fr.recipient == currentUser["idUser"]
        ).order_by(desc(FriendRequest.dateFriendRequest))[selectFriendRequestOffset:selectFriendRequestMax]
    response = {
        "Data" : {}
    }
    for fr in selectFriendRequest:
        response["Data"]["sender"] = fr.sender
        response["Data"]["dateFriendRequest"] = fr.dateFriendRequest
    return responseHandler.ok(response)

@jwt_required
def sendFriendRequest(targetIdUser):
        currentUser = get_jwt_identity()
        if currentUser["idUser"] == targetIdUser:
             response = {
                  "Data": "You cannot send friend request to yourself"
             }
             return responseHandler.badRequest(response)
        selectTargetIdUser = select(u for u in User if u.idUser == targetIdUser)
        if len(selectTargetIdUser) != 0:
            selectFriendRequestFromTargetUser = select(
                 fr for fr in FriendRequest if fr.sender == targetIdUser and fr.recipient == currentUser["idUser"]
            )
            # if target user havent send friend request to current user
            if len(selectFriendRequestFromTargetUser) == 0: 
                selectFriendRequestFromCurrentUser = select(
                    fr for fr in FriendRequest if fr.sender == currentUser["idUser"] and 
                    fr.recipient == targetIdUser)
                if len(selectFriendRequestFromCurrentUser) != 0:
                     selectFriendRequestFromCurrentUser.delete(bulk=True)
                FriendRequestObject = FriendRequest(
                    sender=currentUser["idUser"], recipient="targetIdUser", dateFriendRequest=datetime.now())
                response = {
                    "Data" : "Friend request sent"
                }
                return responseHandler.ok(response)
            # if target user already send friend request to current user, automatically become friend
            else:
                    selectFriendRequestFromTargetUser.delete(bulk=True)
                    selectFriendRequestFromCurrentUser = select(
                    fr for fr in FriendRequest if fr.sender == currentUser["idUser"] and 
                    fr.recipient == targetIdUser)
                    if len(selectFriendRequestFromCurrentUser) != 0:
                        selectFriendRequestFromCurrentUser.delete(bulk=True)
                    # TODO
                    # TODO
        else:
             response = {
                  "Data" : "Target user does not exist"
             }
             return responseHandler.badGateway(response)

