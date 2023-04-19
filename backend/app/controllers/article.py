from flask import request, jsonify, render_template
from app import requestMapping, requestStruct, responseHandler
from flask_jwt_extended import get_jwt_identity, jwt_required
from http import HTTPStatus
from json_checker import Checker
from app.models.content import Content
from app.models.article import Article
from app.models.user import User
from uuid import uuid4
from pony.orm import select
from werkzeug.utils import secure_filename
from app import allowedextensions, uploadFolderContents
import os
from pony.orm import desc
import markdown

ALLOWED_EXTENSIONS = {'md'}



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@jwt_required()
def createArticle():
    try:
        currentUser = get_jwt_identity()
        
        jsonBody = request.form
        data = requestMapping.content(jsonBody)
        result = Checker(requestStruct.content(), soft=True).validate(data)
        if jsonBody["title"] == "":
            response = {
                "Message": "Title Must be Filled"
            }
            return responseHandler.badRequest(response)
        
        file = request.files.get('contentBody')
        if not file or file.name == "" or not allowed_file(file.filename):
            return "no file uploaded"

        filename = secure_filename(file.filename)
        mdFileName = currentUser['idUser'] + '_' + jsonBody["title"] + '_'+ filename
        file.save(os.path.join(uploadFolderContents, mdFileName))
        

        path = os.path.join(uploadFolderContents, mdFileName)
        uuidContent = str(uuid4())
        content = Content(id_content=uuidContent,
                          title=result["title"],
                          subtitle="",
                          img="",
                          captions="",
                          contentBody=path)

        uuidArticle = str(uuid4())
        print(content.id_content)

        article = Article(idArticle=uuidArticle,
                          user=currentUser["idUser"],
                          content=content.id_content)


        data = {
            "idArticle": uuidArticle,
            "title": content.title,
            "contentPath": content.contentBody
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
        selectAllIdArticle = select(str(a.idArticle) for a in Article)[:]
        if id not in selectAllIdArticle:
            response = {
                "message": "Article Not Found"
            }
            return responseHandler.badRequest(response)

        article = Article[id]
        content = select(c for c in Content
                             for a in c.article
                             if str(a.idArticle) == id).first()
        contentPath = content.contentBody

        # filename = os.path(contentPath)

        # print(filename)
        with open(contentPath, 'r') as f:
            markdown_content = f.read()

        html_content = markdown.markdown(markdown_content)
        
        data = {
            "id_article": article.idArticle,
            "title": content.title,
            "contentPath": contentPath,
            "markdown_content": markdown_content,
            "html_content": html_content
        }

        response = {
            "Data": data,
            "message": "successful"
        }

        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY


# def readAllArticle():
#     try:
#         contents = select(c for c in Content)
#         lst = []
#         for content in contents:
#             dct = {
#                 "id_content": content.id_content,
#                 "title": content.title,
#                 "subtitle": content.subtitle,
#                 "img": content.img,
#                 "captions": content.captions,
#                 "contenBody": content.contentBody,
#                 "datePublished": content.datePublished
#             }
#             lst.append(dct)
#         response = {
#             "Data": lst
#         }
#         print("masuk read all artikel")
#         return responseHandler.ok(response)
#     except Exception as err:
#         return str(err), HTTPStatus.BAD_GATEWAY
    
# @jwt_required()
# def updateArticle(id):
#     try:
#         currentUser = get_jwt_identity()
#         # select semua id content by username
#         print(currentUser["username"])
#         selectAllIdContent = select(str(a.content) for a in Article
#                                     for u in a.user
#                                     if u.username == currentUser["username"])[:]
#         print(selectAllIdContent)
#         if id not in selectAllIdContent:
#             response = {
#                 "message": "Article Not Found"
#             }
#             return responseHandler.badRequest(response)

#         jsonbody = request.form
#         data = requestMapping.content(jsonbody)
#         result = Checker(requestStruct.content(), soft=True).validate(data)

#         if jsonbody["title"] == "" or jsonbody["contentBody"] == "" or jsonbody["datePublished"] == "":
#             response = {
#                 "Message": "Title, Content, and Date Publised Must be Filled"
#             }
#             return responseHandler.badRequest(response)

#         file = request.files.get('img')
#         if not file or file.name == "":
#             picfilename = ""

#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             picfilename = currentUser['idUser'] + '_' + filename
#             file.save(os.path.join(uploadFolderContents, picfilename))

#         content = Content[id]
#         content.title = result["title"]
#         content.subtitle = result["subtitle"]
#         content.img = "halo"
#         content.captions = result["captions"]
#         content.contentBody = result["contentBody"]
#         content.datePublished = result["datePublished"]

#         data = {
#             "id_content": content.id_content,
#             "title": content.title,
#             "subtitle": content.subtitle,
#             "img": content.img,
#             "captions": content.captions,
#             "contenBody": content.contentBody,
#             "datePublished": content.datePublished
#         }

#         response = {
#             "Data": data
#         }
#         return responseHandler.ok(response)
#     except Exception as err:
#         return str(err), HTTPStatus.BAD_GATEWAY


# @jwt_required()
# def deleteArticle(id):
#     try:
#         currentUser = get_jwt_identity()
#         # select semua id content by username
#         print(currentUser["username"])
#         selectAllIdContent = select(str(a.content) for a in Article
#                                     for u in a.user
#                                     if u.username == currentUser["username"])[:]

#         if id not in selectAllIdContent:
#             response = {
#                 "message": "Article Not Found"
#             }
#             return responseHandler.badRequest(response)
#         # content = Content[str(id)]
#         Content[id].delete()

#         print("masuk delete artikel")
#         return "delete article"
#     except Exception as err:
#         return str(err), HTTPStatus.BAD_GATEWAY

def userRecentArticle(userId):
    try:
        jsonBody = request.json
        data = requestMapping.userRecentArticle(jsonBody)
        result = Checker(requestStruct.userRecentArticle(), soft=True).validate(data)
        maxArticlePerPage = result["maxArticlePerPage"]
        page = result["page"]
        if maxArticlePerPage == "":
            maxArticlePerPage = 10
        if page == "":
            page = 1
        maxArticlePerPage = int(maxArticlePerPage)
        page = int(page)
        if page <= 0:
            response = {
                "Data": "page must be higher than 0"
            }
            return responseHandler.badRequest(response)
        selectUserArticleOffset = (maxArticlePerPage*(page-1))
        selectUserArticleMax = maxArticlePerPage + selectUserArticleOffset
        selectUserArticle = select(
            a for a in Article for u in a.user if u.idUser == userId).order_by(desc(Article.idArticle))[selectUserArticleOffset:selectUserArticleMax]
        response = {
                "Data" : {}
            }
        for a in selectUserArticle:
            response["Data"]["idArticle"] = a.idArticle
        return responseHandler.ok(response)
    except Exception as err:
        return str(err), HTTPStatus.BAD_GATEWAY
    