from flask import Blueprint
from app.controllers.auth_controller import login

auth_blueprint = Blueprint("auth_blueprint", __name__)

auth_blueprint.route("/login", methods=['POST'])(login)