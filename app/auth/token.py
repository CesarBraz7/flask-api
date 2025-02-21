from flask_jwt_extended import create_access_token, decode_token
import datetime

def generate_token(id):
    return create_access_token(identity=str(id), expires_delta=datetime.timedelta(hours=1))

def get_jwt_identity(token):
    try:
        payload = decode_token(token)
        return payload['identity'] # armazena o id do user
    except Exception:
        return None