from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/formulario', methods=["POST","GET"])
def formulario():
    
    nome = request.form.get('nome')
    idade = request.form.get('idade')
    atividade = request.form.getlist('atividades')
    #atividade = " ".join(atividade)
    if nome is None or idade is None:
        return render_template('formulario.html ')
    else:
        return render_template('dados_recebidos.html', name=nome, idade=idade, atividade=atividade)

app.run(debug=True)