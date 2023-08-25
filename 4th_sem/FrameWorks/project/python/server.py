from flask import Flask, render_template, redirect, url_for
from flask import request, session

from sqlalchemy.sql import text

import cadastro_model

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def principal():
    cadastro_model.criarTabelaUsuario()
    return render_template("entrada.html")

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("name")
        email = request.form.get("email")
        studant = request.form.get("studant")
        aluno = 0
        cpf_cnpj = request.form.get("cnpf")
        birthday = request.form.get("bday")
        number = request.form.get("tel")

        if studant == "on":
            aluno = 1
        else:
            aluno = 2

        if nome =="":
            return "Nome não informado",
        elif email =="":
            return "Email não informado",
        elif cpf_cnpj =="":
            return "CPF/CNPJ não informado"
        elif birthday == "":
            return "Data de nacimento não informada"
        elif number == "":
            return "Número de telefone não informado"

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

@app.route("/registrado")

def registrado():
    dados = eval(request.args.get("dados"))
    if request.method == "POST":
        return render_template("User_registered.html", name=dados["name"], Email=dados["email"], cpf=dados["cpf_cnpj"], niver=dados["birthday"],
            phone=dados["phone"], estudante=dados["user_type_id"])
    return render_template("User_registered.html", name=dados["name"], Email=dados["email"], cpf=dados["cpf_cnpj"], niver=dados["birthday"],
        phone=dados["phone"], estudante=dados["user_type_id"])

app.run(app.run(host = 'localhost', port = 5002, debug = True))