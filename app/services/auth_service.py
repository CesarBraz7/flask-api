from app.auth.token import generate_token
from app.models.user import User


def create(data):
    user = User.query.filter_by(email=data['email']).first() # procura email

    if user and user.check_password(data['password']): # verifica se tem email e checa a senha
        token = generate_token(user.id)
        return token
    
    return None