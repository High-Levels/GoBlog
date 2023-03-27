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
        "subtitle": jsonBody["subtitle"],
        "img": jsonBody["img"],
        "captions": jsonBody["caption"],
        "contentBody": jsonBody["contentBody"],
        "datePublished": jsonBody["datePublished"]
    }
    return data