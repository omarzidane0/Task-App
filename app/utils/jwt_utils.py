from flask_jwt_extended import create_access_token , decode_token

def createtoken(user_id):
    return create_access_token(identity=str(user_id))

def decodetoken(token):
    return decode_token(token)