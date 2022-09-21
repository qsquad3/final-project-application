# APLICAÇÃO QUODE

Aplicação utilizada como docker container no servidor kubernetes.
Ao dar um PUSH nas branch Main, um job é executado via GitHub Action para gerar uma nova versão da imagem e publicar no DockerHUB. O mesmo acontece ao realizar um PULL RESQUEST nas branches Dev, Staging ou Prod.

## Continuos Integration

- O workflow do GitHub Action cria dois jobs: build_official_image, responsável pelo build da imagem da aplicação; e check_image, responsável pelo teste da imagem.

- A branch de PROD está protegida de commits diretos. Só será possível realizar commits para a branch PROD através de Merge Request.

- Tags repetidas estão sendo ignoradas pelo Job. Dentro do step de criação do build da imagem docker (build_official_image), é realizada a criação da tag no step (Bump version and push tag), impossibilitando que se repitam.

## Aplicação Python

Diretório da aplicação: /src

Arquivo principal da aplicação: /src/app.py

Dockerfile da aplicação: /Dockerfile

Arquivo para criação da tabela do banco de dados: create_database.sql

### Variáveis de ambiente para conexão com banco de dados

- As informações de conexão com o banco de dados estão sendo passadas para a aplicação como variável ambiente.

host = os.getenv("DB_HOST")

database = os.getenv("DB_NAME")

user = os.getenv("DB_USER")

password = os.getenv("DB_PASSWD")

## Export de métricas

- As métricas da aplicação sao exportadas via biblioteca:

```from prometheus_flask_exporter import PrometheusMetrics```