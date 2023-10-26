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
    return render_template('comunidade.html', user = user())

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html', user = user())

# Cadastro de usuarios;
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', user = user())

@app.route('/blog-logado')
def blog():
    return render_template('blog-logado.html', user = user())


@app.route('/historia-logado')
def hist():
    return render_template('historia-logado.html', user = user())

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html', user = user())

@app.route('/historia')
def historia():
    return render_template('historia.html', user = user())

@app.route('/perguntasFrequentes')
def perguntasFrequentes():
    with open('static/docs/faq.csv', 'r', encoding= 'UTF-8') as documento:
        texto = documento.readlines()
        
        conteudoFaq = []
        
        for i in range(0, len(texto), 2):
            conteudoFaq.append([texto[i], texto[i+1]])
   
    return render_template('perguntasFrequentes.html', user = user(), conteudoFaq=conteudoFaq)