from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app) # Deixei comentado, para ter a execução é necessário configurar o banco;

from routes.views import *
from routes.autenticar import *
from routes.comunidade import *

if __name__ == '__main__':
    app.run(debug=True) 