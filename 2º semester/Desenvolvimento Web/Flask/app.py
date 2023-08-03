from flask import Flask, render_template
from pessoa import Pessoa

app = Flask(__name__)

@app.route('/aluno')
def aluno():
    Alunos = ['gabriel','igor','lago','ele alí ó']
    eu = Pessoa('Gabriel', 2102341)
    return render_template('aluno.html', nome="Gabriel", nota=9, aluno=Alunos, cara=eu.get_nome(), ra=eu.get_matricula())


app.run(debug=True)

