from flask import request, jsonify
from app import requestMapping, requestStruct, responseHandler
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus
from json_checker import Checker
from app.models.content import Content
from app.models.article import Article
from app.models.user import User
from uuid import uuid4
from pony.orm import select


@jwt_required()
def createArticle():
    try:
        jsonbody = request.json
        data = requestMapping.content(jsonbody)
        result = Checker(requestStruct.content(), soft=True).validate(data)

        if jsonbody["title"] == "" or jsonbody["contentBody"] == "" or jsonbody["datePublished"] == "":
            response = {
                "Message": "Title, Content, and Date Published Must be Filled"
            }
            return responseHandler.badRequest(response)

        uuidContent = str(uuid4())
        content = Content(id_content=uuidContent,
                          title=result["title"],
                          subtitle=result["subtitle"],
                          img=result["img"],
                          captions=result["captions"],
                          contentBody=result["contentBody"],
                          datePublished=result["datePublished"])

        uuidArticle = str(uuid4())
        currentUser = get_jwt_identity()
        print(content.id_content)

        article = Article(idArticle=uuidArticle,
                          user=currentUser["idUser"],
                          content=content.id_content)

        data = {
            "id_content": content.id_content,
            "title": content.title,
            "subtitle": content.subtitle,
            "img": content.img,
            "captions": content.captions,
            "contenBody": content.contentBody,
            "datePublished": content.datePublished
        }
        response = {
            "Data": data,
            "Message": "Article Created"
        }
        return responseHandler.ok(response)
    except Exception as err:
        response = {
            "Error": str(err)
        }
        return responseHandler.badGateway(response)


def readArticle(id):
    try:
        selectAllIdContent = select(str(c.id_content) for c in Content)[:]
        print(id)
        print(selectAllIdContent)
        if id not in selectAllIdContent:
            response = {
                "message": "Article Not Found"
            }
            return responseHandler.badRequest(response)

        content = Content[id]
        data = {
            "id_content": content.id_content,
            "title": content.title,
            "subtitle": content.subtitle,
            "img": content.img,
            "captions": content.captions,
            "contenBody": content.contentBody,
            "datePublished": content.datePublished
        }

        response = {
            "Data": data
        }
        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY

@jwt_required()
def updateArticle(id):
    try:
        currentUser = get_jwt_identity()
        # select semua id content by username
        print(currentUser["username"])
        selectAllIdContent = select(str(a.content) for a in Article 
                                                   for u in a.user
                                                   if u.username == currentUser["username"])[:]
        print(selectAllIdContent)
        if id not in selectAllIdContent:
            response = {
                "message": "Article Not Found"
            }
            return responseHandler.badRequest(response)
              
        jsonbody = request.json
        data = requestMapping.content(jsonbody)
        result = Checker(requestStruct.content(), soft=True).validate(data)

        if jsonbody["title"] == "" or jsonbody["contentBody"] == "" or jsonbody["datePublished"] == "":
            response = {
                "Message": "Title, Content, and Date Publised Must be Filled"
            }
            return responseHandler.badRequest(response)
        
        content = Content[id]
        content.title = result["title"]
        content.subtitle = result["subtitle"]
        content.img = result["img"]
        content.captions = result["captions"]
        content.contentBody = result["contentBody"]
        content.datePublished = result["datePublished"]
        
        data = {
            "id_content": content.id_content,
            "title": content.title,
            "subtitle": content.subtitle,
            "img": content.img,
            "captions": content.captions,
            "contenBody": content.contentBody,
            "datePublished": content.datePublished
        }

        response = {
            "Data": data
        }
        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY

@jwt_required()
def deleteArticle(id):
    try:
        currentUser = get_jwt_identity()
        # select semua id content by username
        print(currentUser["username"])
        selectAllIdContent = select(str(a.content) for a in Article 
                                                   for u in a.user
                                                   if u.username == currentUser["username"])[:]
        if id not in selectAllIdContent:
            response = {
                "message": "Article Not Found"
            }
            return responseHandler.badRequest(response)
        # content = Content[str(id)]
        Content[id].delete()

        print("masuk delete artikel")
        return "delete article"
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY


def readAllArticle():
    try:
        contents = select(c for c in Content)
        lst = []
        for content in contents:
            dct = {
                "id_content": content.id_content,
                "title": content.title,
                "subtitle": content.subtitle,
                "img": content.img,
                "captions": content.captions,
                "contenBody": content.contentBody,
                "datePublished": content.datePublished
            }
            lst.append(dct)
        response = {
            "Data": lst
        }
        print("masuk read all artikel")
        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY
