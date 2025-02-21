# Usa a versão correta do Python
FROM python:3.12.6

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expõe a porta da API
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]
