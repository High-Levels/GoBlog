def User():
    schema = {
        "username": str,
        "email": str,
        "password": str
    }
    return schema

def userUpdate():
    schema = {
        "username": str,
        "email": str,
        "password": str,
        "name": str,
        "gender": str,
        "address": str,
        "birth": str,
        "phoneNumber": str
    }
    return schema

def forgetPassword():
    schema = {
        "password": str,
        "password2": str
    }
    return schema


def Books():
    schema = { 
        # "stock": int,
        "bookTitle": str,
        "bookCategory": str,
        "bookAuthor": str,
        "bookPublisher": str
    }
    return schema

def Authors():
    schema = { 
        "name": str,
        "email": str,
        "gender": str,
        "address": str,
        "phoneNumber": str

    }
    return schema

def Publisher():
    schema = {
        "name": str,
        "email": str,
        "address": str,
        "phoneNumber": str
    }
    return schema

def Category():
    schema = {
        "name": str
    }
    return schema

def Tag():
    schema = {
        "name": str
    }
    return schema

def content():
    schema = {
        "title": str,
        "subtitle": str,
        "img": str,
        "captions": str,
        "contentBody": str,
        "datePublished": str
    }
    return schema

def like():
    schema = {
        "like": bool
    }
    return schema

def comment():
    schema = {
        "commentBody": str,
        "dateComment": str
    }
    return schema

def userRecentArticle():
    schema = {
        "maxArticlePerPage": int,
        "page":int
    }
    return schema

def getUserFriendRequest():
    schema = {
        "maxFriendRequestPerPage": int,
        "page": int
    }
    return schema

def getUserFriend():
    schema = {
        "maxFriendPerPage": int,
        "page": int
    }
    return schema