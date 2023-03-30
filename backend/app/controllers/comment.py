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
        selectComment = select(c for c in Comment if c.idComment == id)[:1]
        if len(selectComment) == 0:
            response = {
            "Message": f"Comment with id {id} not found"
            }
            return responseHandler.badGateway(response)
        selectComment = selectComment[0]
        selectCommentArticle = select(a for a in Article if a.idArticle == selectComment.article)[:1]
        # jika artikel tempat komen berada sudah dihapus
        if len(selectCommentArticle) == 0:
            if selectComment.user == currentUser["idUser"]:          
                Comment[id].delete()
                response = {
                    "Message": "Comment Deleted"
                }
                return responseHandler.ok(response)
            else:
                response = {
                    "Message": "You cannot delete this comment"
                }
                return responseHandler.forbidden(response)
        else:
            selectCommentArticle = selectCommentArticle[0]
            # comment dapat dihapus oleh yang mengepost comment atau pemilik artikel tempat comment berada
            if selectComment.user == currentUser["idUser"] or selectCommentArticle.user == currentUser["idUser"]:
                Comment[id].delete()
                response = {
                    "Message": "Comment Deleted"
                }
                return responseHandler.ok(response)
            else:
                response = {
                    "Message": "You cannot delete this comment"
                }
                return responseHandler.forbidden(response)
    except Exception as err:
        response = {
            "Message": str(err)
        }
        return responseHandler.badGateway(response)

