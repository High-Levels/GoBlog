from app import requestMapping, requestStruct, responseHandler
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from json_checker import Checker
from app.models.comment import Comment
from uuid import uuid4
from pony.orm import select
from app.models.article import Article

@jwt_required()
def createComment(id):
    try:
        selectAllIdArticle = select(str(a.idArticle) for a in Article)[:]
        print(selectAllIdArticle)
        if id not in selectAllIdArticle:
            response = {
                "Message": "Article not found"
            }
            return responseHandler.badRequest(response)
        
        jsonBody = request.json
        data = requestMapping.comment(jsonBody)
        print("berhasil mapping harusnya")
        result = Checker(requestStruct.comment(), soft= True).validate(data)

        if result["commentBody"]=="" or result["dateComment"]=="":
            response = {
                "Message": "Comment Body and Date Comment Must be Filled"
            }
            return responseHandler.badRequest(response)
        
        uuidComment = str(uuid4())
        currentUser = get_jwt_identity()
        comment = Comment(idComment = uuidComment,
                          article = id,
                          user = currentUser["idUser"],
                          commentBody = result["commentBody"],
                          dateComment = result["dateComment"]
                          )
        
        
        
        data = {
            "idComment": comment.idComment,
            "idArticle": id,
            "idUser": currentUser["idUser"],
            "commentBody": comment.commentBody,
            "dateComment": comment.dateComment
        }
        print(data)

        response = {
            "Data": data,
            "Message": "Comment Created"
        }
        return responseHandler.ok(response)
    except Exception as err:
        response = {
            "Message": str(err)
        }
        return responseHandler.badGateway(response)

@jwt_required()
def deleteComment(id):
    try:
        currentUser = get_jwt_identity()
        # Select semua id comment milik username
        selectAllIdComment = select(str(c.idComment) for c in Comment
                                                for u in c.user
                                                if u.username == currentUser["username"])
        
        if id not in selectAllIdComment:
            response = {
                "message": "Comment Not Found"
            }
            return responseHandler.badRequest(response)
        
        Comment[id].delete()

        response = {
            "Message": "Comment Deleted"
        }
        return responseHandler.ok(response)
    except Exception as err:
        response = {
            "Message": str(err)
        }
        return responseHandler.badGateway(response)

