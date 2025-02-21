from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import (
    create_user, delete_user, get_user_by_id, get_users, update_user
)
from app.models.user import User

def register():
    """
    Cadastra um novo usuário

    Endpoint que registra um novo usuário no sistema
    ---
      tags:
        - Usuários
      summary: Cadastra um novo usuário
      parameters:
        - name: body
          in: body
          required: true
          schema:
            type: object
            properties:
              name:
                type: string
                example: "João Silva"
              email:
                type: string
                example: "joao@email.com"
              password:
                type: string
                example: "123456"
              is_admin:
                type: boolean
                example: false
            required:
              - name
              - email
              - password
      responses:
        201:
          description: Usuário criado com sucesso
          schema:
            type: object
            properties:
              message:
                type: string
              id:
                type: integer
        400:
          description: Usuário já existe ou dados inválidos
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('is_admin', False)
    
    if not name or not email or not password:
        return jsonify({"message": "nome, email e senha são obrigatórios"}), 400
    
    new_user = create_user(name, email, password, is_admin)
    
    if not new_user:
        return jsonify({"message": "usuário já existe"}), 400
    
    return jsonify({"message": "usuário criado com sucesso", "id": new_user.id}), 201

@jwt_required()
def get_all_users():
    """
    Retorna todos os usuários.

    Endpoint que busca todos os usuários.
    ---
      security:
        - BearerAuth: []
      tags:
        - Usuários
      summary: Lista todos os usuários
      responses:
        200:
          description: Lista de usuários
          schema:
            type: array
            items:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                email:
                  type: string
                is_admin:
                  type: boolean
    """
    users = get_users()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email, "is_admin": user.is_admin} for user in users]), 200

@jwt_required()
def get_user(id):
    """
    Retorna um usuário específico.

    Endpoint que busca um usuário por meio de seu ID.
    ---
      security:
        - BearerAuth: []
      tags:
        - Usuários
      summary: Obtém um usuário por ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Usuário encontrado
        404:
          description: Usuário não encontrado
    """
    user = get_user_by_id(id)
    if not user:
        return jsonify({"message": "usuário não encontrado"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email, "is_admin": user.is_admin}), 200

@jwt_required()
def edit_user(id):
    """
    Edita um usuário existente

    Endpoint responsável por editar um usuário.
    ---
      security:
        - BearerAuth: []
      tags:
        - Usuários
      summary: Edita um usuário por ID
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
              name:
                type: string
                example: "João Atualizado"
              password:
                type: string
                example: "nova_senha"
              is_admin:
                type: boolean
                example: true
    """
    data = request.get_json()
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    user = User.query.get(id)
    
    if not user:
        return jsonify({"message": "usuário não encontrado"}), 404
    
    result = update_user(user.id, current_user, data.get("name"), data.get("password"), data.get("is_admin"))
    
    if result == "Unauthorized":
        return jsonify({"message": "acesso negado"}), 403
    
    return jsonify({"message": "usuário atualizado com sucesso"}), 200

@jwt_required()
def remove_user(id):
    """
    Remove um usuário existente.

    Endpoint que deleta um usuário do sistema.
    ---
      security:
        - BearerAuth: []
      tags:
        - Usuários
      summary: Deleta um usuário por ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Usuário removido com sucesso
        403:
          description: Acesso negado
        404:
          description: Usuário não encontrado
    """
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    user = User.query.get(id)
    
    if not user:
        return jsonify({"message": "usuário não encontrado"}), 404
    
    result = delete_user(id, current_user)
    
    if result == "Unauthorized":
        return jsonify({"message": "acesso negado"}), 403
    
    return jsonify({"message": "usuário removido com sucesso"}), 200
