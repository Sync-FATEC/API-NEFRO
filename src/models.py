from app import db

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

class Comentarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto_comentario = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    comentario_para = db.Column(db.Integer, nullable=False)
    data_postada = db.column(db.DateTime(timezone=True), default=func.now())