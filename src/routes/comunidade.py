from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import *
import os

def user():
    if 'user' not in session or session['user'] == None:
        user = None
    else:
        user = Usuario.query.filter_by(user_id=session['user']).first()
    return user

@app.route('/postar', methods=["POST"])
def postagem():
    fk_user_id = session['user']
    nome_filho = request.form['nomefilho']
    data_nasc = request.form['dataNascimentoFilho']
    com_historia = request.form['historia']
    imagens = request.files.getlist('upload-input')
    
    img_caminho = ''
    if imagens[0].filename != '':
        for img in imagens:
            name = f'imgHist{len(os.listdir(os.path.join("static", "uploads")))+1}.jpg'
            img.save(os.path.join('static', 'uploads', name))
            img_caminho += f'../static/uploads/{name} '
        img_caminho = img_caminho[:-1]


    usuario = Usuario.query.filter_by(user_id=fk_user_id).first()

    nova_historia = Comentarios(fk_user_id=fk_user_id, com_historia=com_historia, com_nome_filho=nome_filho, com_data=data_nasc)

    if img_caminho != '': nova_historia.com_imagem = img_caminho

    if usuario.user_admin == True:
        nova_historia.com_aprovado = True

    db.session.add(nova_historia)
    db.session.commit()

    return redirect(url_for('comunidade'))

@app.route('/comentar', methods=["POST"])
def comentar():
    usuario = user()
    resposta = request.form['comentario']
    historia = request.form['redirecionar']

    novo_comentario = Comentarios(fk_user_id=usuario.user_id, com_historia=resposta, fk_com_id=historia, com_aprovado=True)

    db.session.add(novo_comentario)
    db.session.commit()

    return redirect(url_for('historia', id=historia))  

@app.route('/aceitar/<id>', methods=['POST', 'GET'])
def aceitar(id):
    historia = Comentarios.query.filter_by(com_id=id).first()
    historia.com_aprovado = True

    db.session.commit()

    return redirect(url_for('admin'))

@app.route('/excluir/<id>', methods=['POST', 'GET'])
def excluir(id):
    historia = Comentarios.query.filter_by(com_id=id).first()
    comentarios = Comentarios.query.filter_by(fk_com_id=id).all()
    for i in comentarios:
        db.session.delete(i)
    db.session.commit()
    db.session.delete(historia)
    db.session.commit()
    
    if 'q' in request.args:
        return redirect(url_for('comunidade'))
    return redirect(url_for('admin'))

@app.route('/reportar/<id>', methods=['POST', 'GET'])
def reportar(id):
    reportar = Comentarios.query.filter_by(com_id=id).first()
    reportar.com_denuncia = True

    db.session.commit()

    return redirect(url_for('historia', id=id))

@app.route('/tirardenuncia/<id>', methods=['POST', 'GET'])
def tirardenuncia(id):
    historia = Comentarios.query.filter_by(com_id=id).first()
    historia.com_denuncia = False

    db.session.commit()

    return redirect(url_for('admin'))