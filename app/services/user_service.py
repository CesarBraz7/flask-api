from app import db
from app.auth.token import generate_token
from app.models.user import User

def create_user(name, email, password, is_admin):
    if User.query.filter_by(email=email).first():
        return None

    new_user = User(
        name = name,
        email = email,
        is_admin = is_admin
    )

    new_user.set_password(password)

    db.session.add(new_user) # adiciona no banco
    db.session.commit()

    return new_user

def get_users():
    return User.query.all()

def get_user_by_id(id):
    return User.query.get(id)

def update_user(id, current_user, name=None, password=None, is_admin=None):
    user = User.query.get(id)

    if not user:
        return None
    
    # verifica se o id do usuario atual é igual ao id do autor do post, verifica também se o usuario atual é um admin ou não
    if current_user.id != user.id and not current_user.is_admin:
        return "Unauthorized"
    
    if name:
        user.name = name
    if password:
        user.password = password
    if is_admin is not None and current_user.is_admin:
        user.is_admin = is_admin

    db.session.commit()
    return user


def delete_user(id, current_user):
    user = User.query.get(id)

    if not user:
        return None
    # verifica se o id do usuario atual é igual ao id do autor do post, verifica também se o usuario atual é um admin ou não
    if current_user.id != user.id and not current_user.is_admin:
        return "Unauthorized"

    db.session.delete(user)
    db.session.commit()

    return True