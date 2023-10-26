from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import *

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/drcBrasil')
def drcBrasil():
    return render_template('drcBrasil.html')

@app.route('/comunidade')
def comunidade():
    return render_template('comunidade.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Cadastro de usuarios;
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/blog-logado')
def blog():
    return render_template('blog-logado.html')


@app.route('/historia-logado')
def hist():
    return render_template('historia-logado.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/perguntasFrequentes')
def perguntasFrequentes():
    with open('static/docs/faq.csv', 'r', encoding= 'UTF-8') as documento:
        texto = documento.readlines()
        
        conteudoFaq = []
        
        for i in range(0, len(texto), 2):
            conteudoFaq.append([texto[i], texto[i+1]])
   
    return render_template('perguntasFrequentes.html', conteudoFaq=conteudoFaq)