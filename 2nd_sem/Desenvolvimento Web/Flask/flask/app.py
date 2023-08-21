from random import randint
from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)

@app.route("/")
def index():
        return render_template('pagina.html')


@app.route("/pessoa")
def pessoa():
    pessoa = Pessoa('Gabriel', 2012341)
    return render_template('alunos.html', aluno=pessoa)


@app.route("/aluno")
def aluno():
    alunos = {'nome': 'Daniel', 'matricula':randint(1111111,9999999), 'nota': 7}
    resposta = render_template('alunos.html',aluno=alunos)
    return resposta


@app.route("/a")
def ola():
    resposta = "<h1> Lagera é brabo fi</h1>"
    resposta += "<p> daniel é bixa<qp>"
    return resposta

@app.errorhandler(404)
def error(error404):
    return render_template('erro.html')


@app.route("/ola")
def olar():
    resposta = "<h1> Daniel traz o Beck</h1>"
    resposta += "<p> tira da meia</p>"
    return resposta

@app.route("/outrapg")
def ashuashu():
    resposta = "<h1> VAMBOOOORAAA</h1>"
    return resposta

@app.route("/curso/<nome_curso>")

def curso(nome_curso):
    if nome_curso == "devweb":
        return "<h1>Bem vindo a disciplina de Dev. Web</h1>"
    elif nome_curso == "poo":
        return "<h1>Bem vindo a de POO</h1>"
    else:
        return "<h1>Pagina não encontrada</h1>"



app.run(debug=True)