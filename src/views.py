from app import app
from flask import render_template, request, redirect, url_for, session, flash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/drcBrasil')
def drcBrasil():
    return render_template('drcBrasil.html')

@app.route('/proadi')
def proadi():
    return render_template('proadi.html')

@app.route('/comunidade')
def comunidade():
    return render_template('comunidade.html')

@app.route('/perguntasFrequentes')
def perguntasFrequentes():
    return render_template('perguntasFrequentes.html')