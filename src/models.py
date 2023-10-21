from app import db

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    data_nasc = db.Column(db.DateTime, nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    parentesco = db.Column(db.String(20), nullable=False)
    profissao = db.Column(db.String(50), nullable=False)
    como_chegou = db.Column(db.String(50), nullable=False)
