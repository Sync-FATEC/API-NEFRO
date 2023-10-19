from app import app
from flask import render_template, request, redirect, url_for, session, flash

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

@app.route('/cadastro', methods=["POST"])
def cadastro():
    # Fazendo requisição do forms no template "cadastro";
    nomeCompleto = request.form["nomeCompleto"]
    dataNascimento = request.form["dataNascimento"]
    cpf = request.form["cpf"]
    endereco = request.form["endereco"]
    email = request.form["email"]
    parentesco = request.form["parentesco"]
    profissao = request.form["profissao"]
    comoChegou = request.form["comoChegou"]
    senha = request.form["senha"]
    confirmarSenha = request.form["confirmarSenha"]

    if senha == confirmarSenha:
        # Jogando as requisições no banco de dados;
        # Cadastro == nome da nossa tabela;
        # Info dentro dos parentes == Nome das nossas colunas;
        novoUsuario = Cadastro(nome=nomeCompleto, data_nasc=dataNascimento, cpf=cpf, endereco=endereco, email=email, parantesco=parentesco, profissao=profissao, como_chegou=comoChegou, senha=senha)
    else:
        print("deu erro")

    return render_template('cadastro.html')

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