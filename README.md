# APLICAÇÃO PYTHON

**Diretório da aplicação**: /app

**Arquivo principal da aplicação**: /app/app.py

**Dockerfile da aplicação**: /app/Dockerfile

**Arquivo para criação da tabela do banco de dados**: create_database.sql


## Instanciando a aplicação via docker-compose:
```
git clone https://github.com/phwebcloud/python_app.git
cd python_app/
docker-compose up --build -d
 ```

Acessar a aplicação na porta 80 do servidor

## Variáveis ambiente para conexão com banco de dados:
host = os.getenv("***DB_HOST***")

database = os.getenv("***DB_NAME***")

user = os.getenv("***DB_USER***")

password = os.getenv("***DB_PASSWD***")