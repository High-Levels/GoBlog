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

def Books(jsonBody):
    data={
        # "stock": jsonBody['stock'],
        "bookTitle": jsonBody['bookTitle'],
        "bookCategory": jsonBody['bookCategory'],
        "bookAuthor": jsonBody['bookAuthor'],
        "bookPublisher": jsonBody['bookPublisher'],
    } 
    return data

def Authors(jsonBody):
    data = { 
        "name": jsonBody['name'],
        "email": jsonBody['email'],
        "gender": jsonBody['gender'],
        "address": jsonBody['address'],
        "phoneNumber": jsonBody['phoneNumber']
    }
    return data

def Publisher(jsonBody):
    data = {
        "name": jsonBody['name'],
        "email": jsonBody['email'],
        "address": jsonBody['address'],
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