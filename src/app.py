from flask import Flask, render_template, request, redirect, url_for
from prometheus_flask_exporter import PrometheusMetrics
import psycopg2
import os
import names

def create_app():
    app = Flask(__name__)
    return app

app = Flask(__name__)
metrics = PrometheusMetrics(app)

## Database Configuration
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWD")

connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

@app.route('/', methods=['GET','POST'])
def index():
    '''
    Método index da aplicação.
    '''
    if request.method == 'POST':
        message = request.form.get("message")
        app.logger.info(message)
        save(message)
    return render_template('index.html', data=read())

@app.route('/healthcheck', methods=['GET'])
def health():
    '''
    Método de Health Check da aplicação.
    '''
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            connect_timeout=1
        )
        connection.close()
        return '{ status: OK }'
    except:
        return False

@app.route('/limpar', methods=['GET'])
def limpa():
    '''
    Método para limpar input da aplicação.
    '''
    if request.method == 'GET':
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        db = connection.cursor()
        db.execute("DELETE from meessagesdev")
        connection.commit()
        db.close()
        connection.close()
    return redirect(url_for('index'))


@app.route('/popular', methods=['GET','POST'])
def popular():
    '''
    Método para popular com dados genéricos a aplicação.
    '''
    for i in range(1000):
        message = names.get_full_name()
        save(message)
    return redirect(url_for('index'))
       
def save(message):
    '''
    Método para salvar informações da aplicação.
    '''
    connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
    cur = connection.cursor()
    sql = "INSERT INTO meessagesdev(message) VALUES(%s);"
    cur.execute(sql, (message,))
    connection.commit()
    cur.close()
    connection.close()

def read():
    '''
    Método para ler informações do BD da aplicação.
    '''
    connection = psycopg2.connect(
           host=host,
           database=database,
           user=user,
           password=password
       )
    db = connection.cursor()
    db.execute("SELECT * FROM meessagesdev")
    data = db.fetchall()
    db.close()
    connection.close()
    return data

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8501)
