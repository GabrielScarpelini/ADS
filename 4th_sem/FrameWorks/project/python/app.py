from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def cadastro():
    return render_template("formCadastro_flask.html")

app.run(debug=True)