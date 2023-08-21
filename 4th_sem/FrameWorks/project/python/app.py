from flask import Flask, render_template, request, session, redirect

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

    return render_template("formCadastro_flask.html") 

app.run(debug=True)