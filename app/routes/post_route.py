from flask import Blueprint
from app.controllers.post_controller import (
    publish, get_all_posts, get_posts_by_id, get_posts_by_author, edit_post, remove_post
)

post_blueprint = Blueprint("post_blueprint", __name__)

post_blueprint.route("/posts", methods=['POST'])(publish)
post_blueprint.route("/posts", methods=['GET'])(get_all_posts)
post_blueprint.route("/posts/<int:id>", methods=['GET'])(get_posts_by_id)
post_blueprint.route("/posts/author/<int:user_id>", methods=['GET'])(get_posts_by_author)
post_blueprint.route("/posts/<int:id>", methods=['PUT'])(edit_post)
post_blueprint.route("/posts/<int:id>", methods=['DELETE'])(remove_post)