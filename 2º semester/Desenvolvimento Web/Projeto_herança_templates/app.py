from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pagina1")
def homepage():
    return render_template('pagina1.html')

@app.route("/pagina2")
def pag2():
    return render_template('pagina2.html')

@app.route("/pagina3")
def pag3():
    return render_template('pagina3.html')




app.run(debug=True)