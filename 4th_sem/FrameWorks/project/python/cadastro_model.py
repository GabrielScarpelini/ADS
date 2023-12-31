from flask import jsonify
from sqlalchemy.sql import text

import conexao_bd

conn = conexao_bd.mySQL_conection()
cursor = conn.cursor()

def criarTabelaUsuario_mysql():
    create_tabela_usuario = """       
        CREATE TABLE IF NOT EXISTS Usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            cpf_cnpj VARCHAR(255) UNIQUE NOT NULL,
            senha CHAR(100) NOT NULL
        )
        """
    cursor.execute(create_tabela_usuario)
    conn.commit()

def criarTabelaTipo_mysql(): #que guardará o tipo se é aluno ow professor    
    statement = """
    CREATE TABLE IF NOT EXISTS Tipo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) UNIQUE NOT NULL
    )
    """
    cursor.execute(statement);
    conn.commit

def inserirUsuario_mysql(usuario):
    nome = usuario['name']
    email = usuario['email']
    cpf = usuario['cpf']
    senha = usuario['senha']
    statement = "INSERT INTO usuario (nome, email, cpf_cnpj, senha) VALUES (%s, %s, %s, %s)"
    values = [nome, email, cpf, senha]
    cursor.execute(statement, values)
    conn.commit()

def loginUser_mysql(email, password):
    statement = text ("SELECT * FROM Usuario WHERE email = %s AND senha= %s",(email, password)) #esse parenteses aqui está passando os params
    rs = cursor.execute(statement)
    usuario = rs.fetchone() 
    print(usuario)
    if usuario == None:
        return None
    # result = [dict(user) for user in usuario]
    return usuario

def populaTabelaTipo_mysql(dic):
    nome = dic['nome']
    statement = "INSERT INTO Tipo (nome) VALUES (%s)"
    values = [nome]
    cursor.execute(statement, values)
    conn.commit()

def inicializaTBTipo_mysql():
    populaTabelaTipo_mysql({"nome":"Aluno"})
    populaTabelaTipo_mysql({"nome":"Professor"})
    populaTabelaTipo_mysql({"nome":"Administrador"})
