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
        
        jsonSend = {
            ["name"] : nome,
            ["email"] : email,
            ["user_type_id"] : aluno,
            ["password"] : 123456,
            ["is_active"] : "1",
            ["cpf_cnpj"] : cpf_cnpj,
            ["terms"] : "1",
            ["birthday"] : birthday,
            ["phone"] : number,
        }


        # return render_template("User_registered.html", name=nome, Email=email, cpf=cpf_cnpj, niver=birthday, phone=number, estudante=aluno)
        return render_template("User_registered.html")

    return render_template("formCadastro_flask.html") 

app.run(debug=True)