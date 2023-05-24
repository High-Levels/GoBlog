def createUser(jsonBody):
    data = {
        "username": jsonBody['username'],
        "email": jsonBody['email'],
        "password": jsonBody['password']
    }
    return data

def userUpdate(jsonBody):
    data = {
        "username": jsonBody['username'],
        "email": jsonBody['email'],
        "password": jsonBody['password'],
        "name": jsonBody['name'],
        "gender": jsonBody['gender'],
        "address": jsonBody['address'],
        "birth": jsonBody['birth'],
        "phoneNumber": jsonBody['phoneNumber']
    }
    return data

def forgetPassword(jsonBody):
    data = {
        "password": jsonBody['password'],
        "password2": jsonBody['password2']
    }
    return data


def Category(jsonBody):
    data = {
        "name": jsonBody['name']
    }
    return data

def Tag(jsonBody):
    data = {
        "name": jsonBody['name']
    }
    return data

def content(jsonBody):
    data = {
        "title": jsonBody["title"],
        # "subtitle": jsonBody["subtitle"],
        # "img": jsonBody["img"],
        # "captions": jsonBody["caption"],
        # "contentBody": jsonBody["contentBody"],
        # "datePublished": jsonBody["datePublished"]
    }
    return data

def like(jsonBody):
    data = {
        "like": jsonBody["like"]
    }
    return data

def comment(jsonBody):
    data = {
        "commentBody": jsonBody["commentBody"],
        "dateComment": jsonBody["dateComment"]
    }
    return data

def userRecentArticle(jsonBody):
    data = {
        "maxArticlePerPage": jsonBody["maxArticlePerPage"],
        "page": jsonBody["page"]
    }
    return data

def getUserFriendRequest(jsonBody):
    data = {
        "maxFriendRequestPerPage": jsonBody["maxFriendRequestPerPage"],
        "page": jsonBody["page"]
    }
    return data

def getUserFriend(jsonBody):
    data = {
        "maxFriendPerPage": jsonBody["maxFriendPerPage"],
        "page": jsonBody["page"]
    }
    return data

def getUserNotification(jsonBody):
    data = {
        "maxNotificationPerPage": jsonBody["maxNotificationPerPage"],
        "page" : jsonBody["page"]
    }
    return data