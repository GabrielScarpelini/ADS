from flask import Flask, render_template, redirect, url_for
from flask import request, session

from sqlalchemy.sql import text

import cadastro_model

app = Flask(__name__)

@app.route("/", methods=["GET","POST"]) #laguinho monstro
def principal():
    cadastro_model.criarTabelaTipo()
    cadastro_model.criarTabelaUsuario()
    
    if request.method == "POST":
        email = request.form.get("login")
        password = request.form.get("senha")
        cadastrado = cadastro_model.loginUser(email, password)
        print(cadastrado)
        if cadastrado:
           return cadastrado.email
        else:
            return 'uwu'

    return render_template("entrada.html")

@app.route("/inicia")
def inicia():
    cadastro_model.inicializaTBTipo()
    return "Tabela Tipo Atualizada"


@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("name")
        email = request.form.get("email")
        studant = request.form.get("studant")
        aluno = 0
        cpf_cnpj = request.form.get("cnpf")
        number = request.form.get("tel")

        if studant == "on":
            aluno = 1
        else:
            aluno = 2

        if not email and nome and cpf_cnpj and number:
            return 'operação inválida'

        jsonUser = {}
        jsonUser["name"] = nome
        jsonUser["email"] = email
        jsonUser["user_type_id"] = aluno
        jsonUser["password"] = 123456
        jsonUser["is_active"] = "1"
        jsonUser["cpf_cnpj"] = cpf_cnpj
        jsonUser["phone"] = number
        cadastro_model.inserirUsuario(jsonUser)

        return redirect(url_for("registrado", dados=jsonUser))

    return render_template("formCadastro_flask.html") 

@app.route("/registrado", methods=['POST', "GET"])

def registrado():   
    dados = eval(request.args.get("dados"))
    if request.method == "POST":
        return render_template("User_registered.html", name=dados["name"], Email=dados["email"], cpf=dados["cpf_cnpj"],
            phone=dados["phone"], estudante=dados["user_type_id"])
    return render_template("User_registered.html", name=dados["name"], Email=dados["email"], cpf=dados["cpf_cnpj"],
        phone=dados["phone"], estudante=dados["user_type_id"])

app.run(app.run(host = 'localhost', port = 5002, debug = True))