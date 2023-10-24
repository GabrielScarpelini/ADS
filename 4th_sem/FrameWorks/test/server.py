from flask import Flask, render_template, redirect, url_for
from flask import request, session

app = Flask(__name__)

@app.route("/")
def inicia():   
    dados = ["zdaYlEcfG7w", "zdaYlEcfG7w", "zdaYlEcfG7w"]
    if request.method == "POST":
        return render_template("index.html", dados=dados)
    return render_template("index.html", dados=dados)

app.run(app.run(host = 'localhost', port = 5002, debug = True))