from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import *

def user():
    if 'user' not in session or session['user'] == None:
        user = None
    else:
        user = Usuario.query.filter_by(user_id=session['user']).first()
    return user

@app.route('/')
def index():
    return render_template('home.html', user = user())

@app.route('/drcBrasil')
def drcBrasil():
    return render_template('drcBrasil.html', user = user())

@app.route('/comunidade')
def comunidade():

    filtro = Comentarios.query.filter(Comentarios.fk_com_id.is_(None)).all()

    # filtro = filtro.sorted(filtro, reverse=True)
    print(filtro)

    return render_template('comunidade.html', user = user(), comentarios=filtro, Usuario=Usuario)

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html', user = user())

# Cadastro de usuarios;
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', user = user())

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html', user = user())

@app.route('/historia/<id>')
def historia(id):
    comentario = Comentarios.query.filter_by(com_id=id).first()
    respostas = Comentarios.query.filter_by(fk_com_id=id).all()
    return render_template('historia.html', user = user(), respostas=respostas, comentario=comentario, Usuario=Usuario)

@app.route('/perguntasFrequentes')
def perguntasFrequentes():
    with open('static/docs/faq.csv', 'r', encoding= 'UTF-8') as documento:
        texto = documento.readlines()
        
        conteudoFaq = []
        
        for i in range(0, len(texto), 2):
            conteudoFaq.append([texto[i], texto[i+1]])
   
    return render_template('perguntasFrequentes.html', user = user(), conteudoFaq=conteudoFaq)

@app.route('/admin')
def admin():
    usuario = user()
    if usuario == None or not usuario.user_admin:
        flash('Você não tem acesso a essa pagina')
        return redirect(url_for('index'))
    publicacoes = Comentarios.query.filter_by(com_denuncia=True).all()
    return render_template('admin.html', user = user(), publicacoes=publicacoes)