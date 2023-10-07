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
    dicionario = {'O que é IRC (Insuficiência Renal Crônica?':
'A IRC é uma condição médica em que os rins perdem gradualmente a capacidade de filtrar resíduos e excesso de líquidos do sangue, levando a problemas de saúde sérios e duradouros.',
'Quais são as principais causas da IRC?':
'As causas mais comuns da IRC incluem hipertensão arterial, diabetes, doenças renais hereditárias, infecções renais crônicas e obstruções no trato urinário.',
'Quais são os sintomas da IRC?':
'Os sintomas podem variar, mas os mais comuns incluem fadiga, inchaço nas pernas e tornozelos, pressão alta, dificuldade para concentrar a urina, aumento da frequência urinária e anemia.',
'Como a IRC é diagnosticada?':
'O diagnóstico envolve exames de sangue para medir os níveis de creatinina e ureia, além de exames de imagem, como ultrassonografia ou tomografia, e biópsia renal, em alguns casos.',
'Qual é o tratamento para a IRC?':
'O tratamento pode incluir mudanças na dieta, controle de pressão arterial, medicamentos para aliviar sintomas, diálise e, em casos graves, transplante renal.',
'Como posso prevenir a IRC?':
'Prevenir a IRC envolve controlar condições de saúde subjacentes, como diabetes e hipertensão, evitar o uso excessivo de medicamentos que podem prejudicar os rins, manter uma dieta saudável e ficar bem hidratado.',
'Qual é a expectativa de vida de alguém com IRC?':
'A expectativa de vida varia dependendo da gravidade da IRC e da resposta ao tratamento. Com tratamento adequado, muitas pessoas com IRC podem levar vidas satisfatórias e produtivas. O transplante renal pode ser uma opção que melhora significativamente a qualidade de vida.',
'O que é a diálise e como funciona no tratamento da IRC?':
'A diálise é um procedimento médico que filtra resíduos e excesso de líquidos do sangue quando os rins não conseguem fazê-lo. Existem dois tipos principais: hemodiálise, realizada em uma clínica especializada, e diálise peritoneal, que pode ser feita em casa. Ambos ajudam a manter o equilíbrio do corpo quando os rins não funcionam adequadamente.'}
    return render_template('perguntasFrequentes.html', dicionario = dicionario)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')