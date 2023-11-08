from app import app, db
from flask import render_template, request, redirect, url_for, session, flash
from models import *

def user():
    if 'user' not in session or session['user'] == None:
        user = None
    else:
        user = Usuario.query.filter_by(user_id=session['user']).first()
    return user


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
    elif Usuario.query.filter_by(user_cpf=cpf).first():
        flash("O cpf inserido já existe, Faça login!")
        return redirect(url_for('login'))
    
    elif len(cpf) > 11:
        flash("Número de caracteres do cpf inválido!")
        return redirect(url_for('cadastro'))
    
    elif len(nomeCompleto) > 100:
        flash("Você passou o número maximo de caracteres permitidos no nome!")
        return redirect(url_for('cadastro'))
    
    elif len(endereco) > 100:
        flash("Você passou o número maximo de caracteres permitidos no endereço!")
        return redirect(url_for('cadastro'))
    
    elif len(email) > 100:
        flash("Você passou o número maximo de caracteres permitidos no email!")
        return redirect(url_for('cadastro'))
    
    elif len(profissao)  > 50:
        flash('Você passou o número maximo de caracteres permitidos na profissão ou no como chegou!')
        return redirect(url_for('cadastro'))
    
    elif len(comoChegou)  > 50:
        flash('Você passou o número maximo de caracteres permitidos no como chegou!')
        return redirect(url_for('cadastro'))
    
    elif len(parentesco) > 20:
        flash('Você passou o número maximo de caracteres permitidos no parentesco!')
        return redirect(url_for('cadastro'))
    
    elif len(senha) > 26:
        flash('Você atingiu o número maximo de caracteres permitidos na senha!')
        return redirect(url_for('cadastro'))
    
    # Verificando se as senhas são iguais;
    elif senha == confirmarSenha:
        # Jogando as requisições no banco de dados;
        novoUsuario = Usuario (user_nome=nomeCompleto, user_data_nasc=dataNascimento, user_cpf=cpf, user_endereco=endereco, user_email=email, user_parentesco=parentesco, user_profissao=profissao, user_como_chegou=comoChegou, user_senha=senha)

        db.session.add(novoUsuario)
        db.session.commit()

        session["user"] = novoUsuario.user_id

    else:
         flash('As senhas devem ser identicas!')
         return redirect(url_for('cadastro'))

         

    # Redirecionando para homepage;     
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session['user'] = None

    return redirect(url_for('index'))

@app.route('/logar', methods=['POST'])
def logar():
    email = request.form['email']
    senha = request.form['senha']

    if not Usuario.query.filter_by(user_email=email).first():
        flash('Email inexistente')
        return redirect(url_for('login'))
    elif Usuario.query.filter_by(user_email=email).first().user_senha != senha:
        flash('Senha incorreta')
        return redirect(url_for('login'))
    else:
        session['user'] = Usuario.query.filter_by(user_email=email).first().user_id
        return redirect(url_for('index'))