from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login():
    if request.method == "POST":
        request.form.get("email")
    
    return render_template("login.html")