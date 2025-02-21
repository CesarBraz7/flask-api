from flask import jsonify, request
from flasgger import swag_from
from app.services.auth_service import create

def login():
    """
    Autenticação do usuário.

    Endpoint para login de usuários e geração de token JWT.

    ---
    tags:
      - Autenticação
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: "user@example.com"
            password:
              type: string
              example: "strongpassword"
          required:
            - email
            - password
    responses:
      200:
        description: Login realizado com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                access_token:
                  type: string
                  example: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      401:
        description: Credenciais inválidas
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Credenciais inválidas"
    """
    data = request.get_json()

    token = create(data)
    if not token:
        return jsonify({"message": "Credenciais inválidas"}), 401

    return jsonify({"access_token": token}), 200