# Social API

## Descrição
Social API é uma API desenvolvida com Flask para gerenciar usuários e posts. A aplicação utiliza SQLAlchemy como ORM, MySQL como banco de dados e JWT para autenticação. A documentação da API é gerada com Swagger.

## Tecnologias Utilizadas
- Flask
- SQLAlchemy
- MySQL
- Swagger
- Docker
- JWT

## Estrutura do Projeto
```
/social_api
│── /app
│   │── /controllers
│   │   ├── auth_controller.py
│   │   ├── user_controller.py
│   │   ├── post_controller.py
│   │── /models
│   │   ├── user.py
│   │   ├── post.py
│   │── /routes
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   ├── post_routes.py
│   │── /services
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── post_service.py
│   │── __init__.py
│── /config
│   ├── settings.py
│   ├── swagger_config.py
│── .env
│── .gitignore
│── docker-compose.yml
│── Dockerfile
│── requirements.txt
│── wait-for-it.sh
│── run.py
│── README.md
```

## Instalação e Execução
A instalação e execução são feitas utilizando Docker. Certifique-se de ter o Docker instalado antes de prosseguir.

### Passos:
1. Clone este repositório:
   ```sh
   git clone https://github.com/CesarBraz7/flask-api.git
   cd social-api
   ```
2. Crie um arquivo `.env` na raiz do projeto com as configurações necessárias (veja a seção de variáveis de ambiente abaixo).
3. Construa e execute os containers:
   ```sh
   docker-compose up --build
   ```

A API estará rodando em `http://127.0.0.1:5000/` e a documentação do Swagger pode ser acessada em `http://127.0.0.1:5000/apidocs/`.

## Banco de Dados
A API utiliza um container Docker para o banco de dados MySQL. Certifique-se de que as variáveis de ambiente estão corretamente configuradas antes de iniciar a aplicação.

## Documentação da API
A documentação da API é gerada automaticamente com Swagger e pode ser acessada em:
```
http://127.0.0.1:5000/apidocs/
```

## Autenticação
A autenticação na API é feita via JWT. Certifique-se de enviar um token JWT válido nos headers das requisições que exigem autenticação.

## Variáveis de Ambiente
A aplicação utiliza um arquivo `.env` para configurar variáveis sensíveis. Abaixo está um exemplo do arquivo `.env` utilizado:

```
MYSQL_ROOT_PASSWORD=0000
MYSQL_DATABASE=social_db
MYSQL_USER=root
MYSQL_PASSWORD=0000

DATABASE_URL=mysql+pymysql://root:0000@db:3306/social_db

SECRET_KEY=8672bce98b346ccb468a6579f8c838d80735c6686ade160f004f3b4705cf17d5
JWT_SECRET_KEY=12afe3914c6815b4e9043bab8aba0b1539f22e5fdccf711c0744fff1e081def8
```

Certifique-se de criar o arquivo `.env` na raiz do projeto e preencher os valores conforme necessário antes de rodar a aplicação.
