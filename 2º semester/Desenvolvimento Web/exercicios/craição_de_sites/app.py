from flask import Flask, render_template

app = Flask(__name__)

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route('/disciplinas')
def disciplinas():
    return render_template('disciplinas.html')

@app.route('/index')
def index():
    return render_template('index.html')

app.run(debug=True)
