from flask import request, jsonify
from app import requestMapping, requestStruct, responseHandler
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus
from json_checker import Checker
from app.models.like import Like
from app.models.user import User
from app.models.article import Article
from uuid import uuid4
from pony.orm import select

@jwt_required()
def readLike(id):
    try:
        currentUser = get_jwt_identity()
        selectArticleById = select(a for a in Article if a.idArticle == id)[:1]
        if len(selectArticleById) == 0:
            response = {
                "message": "Article Not Found"
            }
            return responseHandler.badRequest(response)
        article = selectArticleById[0]
        selectLikeByUserId = select(l for l in Like if l.user == currentUser['idUser'])[:1]
        like = None
        if len(selectLikeByUserId) == 0:
            uuidLike = str(uuid4())
            like = Like(idLike=uuidLike,
                           user=currentUser['idUser'],
                           article=id,
                           like=False)
        else:
            like = selectLikeByUserId[0]
        data = {
            "idLike": like.idLike,
            "user": like.user,
            "article": like.article,
            "like": like.like
        }
        response = {
            "Data": data
        }
        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY

@jwt_required()
def updateLike(id):
    try:
        currentUser = get_jwt_identity()
        selectArticleById = select(a for a in Article if a.idArticle == id)[:1]
        if len(selectArticleById) == 0:
            response = {
                "message": "Article Not Found"
            }
            return responseHandler.badRequest(response)
        article = selectArticleById[0]
        jsonBody = request.json
        data = requestMapping.like(jsonBody)
        result = Checker(requestStruct.like(), soft=True).validate(data)
        if data["like"].lower() != "true" and data["like"].lower() != "false":
            response = {
                "Message": "Like must be \"true\" or \"false\" (case insensitive)"
            }
            return responseHandler.badRequest(response)
        likeBool = None
        if data["like"].lower() == "true":
            likeBool = True
        else:
            likeBool = False
        selectLikeByUserId = select(l for l in Like if l.user == currentUser['idUser'])[:1]
        like = None
        if len(selectLikeByUserId) == 0:
            uuidLike = str(uuid4())
            like = Like(idLike=uuidLike,
                           user=currentUser['idUser'],
                           article=id,
                           like=likeBool)
        else:
            like = selectLikeByUserId[0]
            like.set(like=likeBool)
        data = {
            "idLike": like.idLike,
            "user": like.user,
            "article": like.article,
            "like": like.like
        }
        response = {
            "Data": data
        }
        return responseHandler.ok(response)

        
        
        response = {
            "Data": data
        }
        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY