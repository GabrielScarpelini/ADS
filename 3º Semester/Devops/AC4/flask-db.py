import os
from flask import Flask, render_template, json, request, jsonify # sereliaziação
from flaskext.mysql import MySQL
#from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = 'db'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.7'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('cadastro.html')

@app.route('/gravar',methods=['POST','GET'])
def gravar():

    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    print(nome)
    print(email)
    print(senha)
    if nome and email and senha:
        conn = mysql.connect()
        cursor = conn.cursor()
        hashed_password = senha
        cursor.execute('insert into tbl_user (user_name, user_username, user_password) VALUES (%s, %s, %s)', (nome, email, senha))
        conn.commit()

    return render_template('cadastro.html')

@app.route('/listjson',methods=['POST','GET'])
def listjson():
    try:
            conn = mysql.connect()
            cur = conn.cursor()
            cur.execute ('select user_name from tbl_user') 
            data = cur.fetchall()
            print(data[0]);
            for x in range(len(data)):
                print(data[x])

            conn.commit()
            return jsonify(data)

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cur.close() 
        conn.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
