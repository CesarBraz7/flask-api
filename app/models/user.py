from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    author_posts = db.relationship('Post', back_populates='author', lazy=True) # retorna posts do autor a partir da tabela de posts

    # metodo para adicionar senha já hasheada
    def set_password(self, pw):
        self.password = generate_password_hash(pw)

    # checa a senha enviada com a senha hasheada
    def check_password(self, pw):
        return check_password_hash(self.password, pw)