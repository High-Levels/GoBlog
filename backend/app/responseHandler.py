from http import HTTPStatus
from flask import make_response,jsonify
from flask import redirect

def ok(data):
    return make_response(jsonify(data)),HTTPStatus.OK.value

def badRequest(data):
    return make_response(jsonify(data)),HTTPStatus.BAD_REQUEST.value

def badGateway(data):
    return make_response(jsonify(data)),HTTPStatus.BAD_GATEWAY.value

def forbidden(data):
    return make_response(jsonify(data)),HTTPStatus.FORBIDDEN.value