from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from
from app.models.post import Post
from app.models.user import User
from app.services.post_service import (
    create_post, get_posts, get_post_by_id, get_posts_by_user_id, update_post, delete_post
)

@jwt_required()
def publish():
    """
    Publica um novo post.

    Endpoint responsável por publicar um novo post na rede.
    ---
    security:
      - BearerAuth: []
    tags:
      - Posts
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            post:
              type: string
              example: Novo post
          required:
            - post
    responses:
      201:
        description: "Post publicado com sucesso"
      400:
        description: "Requisição inválida - corpo da requisição vazio"
    """
    data = request.get_json()
    current_user = get_jwt_identity()
    post = data.get("post")
    if not post:
        return jsonify({"message": "impossível postar algo vazio"}), 400
    publish = create_post(current_user, post)
    return jsonify({"message": "publicado com sucesso", "post": publish.post}), 201

@jwt_required()
def get_all_posts():
    """
    Obtém todos os posts.

    Endpoint que retorna todos os posts disponíveis.
    ---
    security:
      - BearerAuth: []
    tags:
      - Posts
    responses:
      200:
        description: "Lista de posts retornada com sucesso"
      404:
        description: "Nenhum post encontrado"
    """
    posts = get_posts()
    if not posts:
        return jsonify({"message": "não há posts"}), 404
    return jsonify([{ "id": post.id, "post": post.post, "author_id": post.author.id, "author_name": post.author.name } for post in posts]), 200

@jwt_required()
def get_posts_by_id(id):
    """
    Obtém um post pelo ID.

    Endpoint que busca um post por meio de seu ID.
    ---
    security:
      - BearerAuth: []
    tags:
      - Posts
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: "Post encontrado"
      404:
        description: "Post não encontrado"
    """
    post = get_post_by_id(id)
    if not post:
        return jsonify({"message": "post não encontrado"}), 404
    return jsonify({"id": post.id, "post": post.post, "author_id": post.author.id, "author_name": post.author.name}), 200

@jwt_required()
def get_posts_by_author(user_id):
    """
    Obter post por autor.

    Endpoint que retorna todos os posts de um determinado autor.
    ---
    security:
      - BearerAuth: []
    tags:
      - Posts
    parameters:
      - name: user_id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: "Lista de posts do autor"
      404:
        description: "Nenhum post encontrado para esse usuário"
    """
    posts = get_posts_by_user_id(user_id)
    if not posts:
        return jsonify({"message": "nenhum post encontrado para esse usuario"}), 404
    return jsonify([{ "id": post.id, "post": post.post, "author_id": post.author.id, "author_name": post.author.name } for post in posts]), 200

@jwt_required()
def edit_post(id):
    """
    Edição de post
    
    Endpoint para editar um post existente.
    ---
    security:
      - BearerAuth: []
    tags:
      - Posts
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            post:
              type: string
              example: Post atualizado
          required:
            - post
    responses:
      200:
        description: "Post atualizado com sucesso"
      403:
        description: "Acesso negado"
      404:
        description: "Post não encontrado"
    """
    data = request.get_json()
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    post = Post.query.get(id)
    if not post:
        return jsonify({"message": "post não encontrado"}), 404
    result = update_post(post.id, current_user, data.get('post'))
    if result == "Unauthorized":
        return jsonify({"message": "acesso negado"}), 403
    return jsonify({"message": "post atualizado com sucesso"}), 200

@jwt_required()
def remove_post(id):
    """
    Remove um post existente.

    Endpoint que deleta um post do sistema.
    ---
    security:
      - BearerAuth: []
    tags:
      - Posts
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: "Post removido com sucesso"
      403:
        description: "Acesso negado"
      404:
        description: "Post não encontrado"
    """
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    post = Post.query.get(id)
    if not post:
        return jsonify({"message": "post não encontrado"}), 404
    result = delete_post(id, current_user)
    if result == "Unauthorized":
        return jsonify({"message": "acesso negado"}), 403
    return jsonify({"message": "post removido com sucesso"}), 200
