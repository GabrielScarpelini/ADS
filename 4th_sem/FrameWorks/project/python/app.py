from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def principal():
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
        
        jsonSend = {}
            
        jsonSend["name"] = nome
        jsonSend["email"] = email
        jsonSend["user_type_id"] = aluno
        jsonSend["password"] = 123456
        jsonSend["is_active"] = "1"
        jsonSend["cpf_cnpj"] = cpf_cnpj
        jsonSend["terms"] = "1"
        jsonSend["birthday"] = birthday
        jsonSend["phone"] = number
        

        return redirect(url_for("showRegisdtred", dados=jsonSend))

    return render_template("formCadastro_flask.html") 

@app.route("/registrado")
def showRegisdtred():
    dados = eval(request.args.get("dados"))
    # return str(type(dados))
    return render_template("User_registered.html", name=dados["name"], Email=dados["email"], cpf=dados["cpf_cnpj"], niver=dados["birthday"],
    phone=dados["phone"], estudante=dados["user_type_id"])

app.run(debug=True)