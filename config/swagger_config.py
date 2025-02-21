swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Social API",
        "description": "Documentação da API",
        "version": "1.0.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Adicione 'Bearer <seu_token>'"
        }
    }
}