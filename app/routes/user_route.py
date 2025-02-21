from flask import Blueprint
from app.controllers.user_controller import (
    register, get_all_users, get_user, edit_user, remove_user
)

user_blueprint = Blueprint("user_blueprint", __name__)

user_blueprint.route("/register", methods=['POST'])(register)
user_blueprint.route("/users/<int:id>", methods=['GET'])(get_user)
user_blueprint.route("/users", methods=['GET'])(get_all_users)
user_blueprint.route("/users/<int:id>", methods=['PUT'])(edit_user)
user_blueprint.route("/users/<int:id>", methods=['DELETE'])(remove_user)