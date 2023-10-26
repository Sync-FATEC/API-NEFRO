from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import *

@app.route('/cadastrar', methods=["POST"])
def cadastrar():
    
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

    # Verificando se o e-mail ja existe no banco;
    if Usuario.query.filter_by(user_email=email).first():
        flash("O email inserido já existe, Faça login!")
        return redirect(url_for('login'))
    
    # Verificando se o cpf ja existe no banco;
    if Usuario.query.filter_by(user_cpf=cpf).first():
        flash("O cpf inserido já existe, Faça login!")
        return redirect(url_for('login'))

    # Verificando se as senhas são iguais;
    if senha == confirmarSenha:
        # Jogando as requisições no banco de dados;
        # Cadastro == nome da nossa tabela;
        # Info dentro dos parentes == Nome das nossas colunas;
        novoUsuario = Usuario (user_nome=nomeCompleto, user_data_nasc=dataNascimento, user_cpf=cpf, user_endereco=endereco, user_email=email, user_parentesco=parentesco, user_profissao=profissao, user_como_chegou=comoChegou, user_senha=senha)
        db.session.add(novoUsuario)
        db.session.commit()
    else:
         flash('As senhas devem ser identicas!')


    # Redirecionando para homepage;     
    return redirect(url_for('index'))

    