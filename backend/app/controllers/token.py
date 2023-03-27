from flask_jwt_extended import jwt_required,get_jwt_identity,create_access_token
from flask import jsonify

@jwt_required(refresh = True)
def refresh():
    currentUser = get_jwt_identity()
    accessToken = create_access_token(identity=currentUser,fresh=True)
    return jsonify(accessToken = accessToken)