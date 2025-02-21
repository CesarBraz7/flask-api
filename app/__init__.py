from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config.settings import Config
from flasgger import Swagger
from config.swagger_config import swagger_template

db = SQLAlchemy()
jwt = JWTManager()
swagger = Swagger(template=swagger_template)

def create_app():
    app = Flask(__name__) # inicia flask
    app.config.from_object(Config) # importa configurações

    db.init_app(app) # inicia banco
    jwt.init_app(app) # inicia jwt
    swagger.init_app(app)

    from app.models import user, post # importa models

    # registra rotas
    from app.routes.user_route import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api')

    from app.routes.post_route import post_blueprint
    app.register_blueprint(post_blueprint, url_prefix='/api')

    from app.routes.auth_route import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api')

    return app
