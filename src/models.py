from app import db
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.sql import func

class Usuario(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_nome = db.Column(db.String, nullable=False)
    user_data_nasc = db.Column(db.DateTime, nullable=False)
    user_endereco = db.Column(db.String(255), nullable=False)
    user_cpf = db.Column(db.String(11), nullable=False)
    user_email = db.Column(db.String, nullable=False)
    user_senha = db.Column(db.String, nullable=False)
    user_parentesco = db.Column(db.String(20), nullable=False)
    user_profissao = db.Column(db.String(50), nullable=False)
    user_como_chegou = db.Column(db.String(50), nullable=False)
    user_admin = db.Column(db.Boolean, default=False)

class Comentarios(db.Model):
    com_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    com_historia = db.Column(db.Text, nullable=False)
    com_data = db.Column(db.Date, nullable=True)
    com_imagem = db.Column(db.String(255), nullable=True)
    com_nome_filho = db.Column(db.String(255), nullable=True)
    com_aprovado = db.Column(db.Boolean, default=False)
    com_denuncia = db.Column(db.Boolean, default=False)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('usuario.user_id'), nullable=True)
    fk_com_id = db.Column(db.Integer, db.ForeignKey('comentarios.com_id'), nullable=True)