from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from json_checker import Checker
from app.models.notification import Notification
from uuid import UUID, uuid4
from pony.orm import select
from datetime import datetime
from app import responseHandler
from app import requestMapping, requestStruct



@jwt_required()
def getRecentNotification():
    response = {
        "notificationList": [],
        "error": False,
        "logMsg": ""
    }
    try:
        currentUser = get_jwt_identity()
        requestJson = request.json
        for key in requestStruct.getUserNotification():
            if key not in requestJson:
                response["error"] = True
                response["logMsg"] = f"Key \"{key}\" is not in request form"
                return responseHandler.badRequest(response)
            elif requestJson[key] == "":
                response["error"] = True
                response["logMsg"] = f"Request form key \"{key}\" value is blank"
        requestJsonDict = requestMapping.getUserNotification(requestJson)
        requestJsonVerified = Checker(requestStruct.getUserNotification, soft=True).validate(requestJsonDict)
        maxNotificationPerPage = int(requestJsonVerified["maxNotificationPerPage"])
        page = int(requestJsonVerified["page"])
        if page <= 0:
            response["error"] = True
            response["logMsg"] = "Page must be bigger than 0"
        selectUserNotificationOffset = maxNotificationPerPage*(page-1)
        selectUserNotificationMax = selectUserNotificationOffset + maxNotificationPerPage
        selectUserNotification = select(notif for notif in Notification 
                                        if notif.receiver.idUser == UUID(currentUser["idUser"])
                                        )[selectUserNotificationOffset:selectUserNotificationMax]
        for notif in selectUserNotification:
            response["notificationList"].apppend({
                "idNotification": str(notif.idNotification),
                "notificationType": notif.notificationType,
                "alreadyRead": notif.alreadyRead,
                "notificationJson": notif.notificationJson,
                "notificationDate": notif.notificationDate
            })
        return responseHandler.ok(response)

    except Exception as e:
        response["error"] = True
        response["logMsg"] = str(e)
        print(e)
        return responseHandler.badGateway(e)



# The function below is for server internal use and are not meant to be put at route.py
def newNotification(receiver, notificationType, notificationJson, notificationDate):
    response = {
        "error":False,
        "logMsg":""
    }
    NotificationObject = Notification(idNotification=uuid4(), 
                                      receiver=receiver, 
                                      notificationType=notificationType,
                                      alreadyRead=False,
                                      notificationJson=notificationJson,
                                      notificationDate=notificationDate)
    return response