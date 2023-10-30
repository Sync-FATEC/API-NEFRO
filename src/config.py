SECRET_KEY = 'API'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '180355',
        servidor = 'localhost',
        database = 'Api'
    )