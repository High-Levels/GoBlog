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