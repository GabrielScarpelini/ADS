from flask import jsonify
from sqlalchemy.sql import text

import conexao_bd

engine = conexao_bd.getConexao()


conn = conexao_bd.mySQL_conection()
cursor = conn.cursor()

def criarTabelaUsuario_mysql():
    create_tabela_usuario = """       
        CREATE TABLE IF NOT EXISTS usuario (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            cpf_cnpj VARCHAR(255) UNIQUE NOT NULL,
            senha CHAR(15) NOT NULL                                                                                                                           
        )
        """
    cursor.execute(create_tabela_usuario)
    conn.commit()

def inserirUsuario_mysql(usuario):
    nome = usuario['name']
    email = usuario['email']
    cpf = usuario['cpf']
    senha = usuario['senha']
    statement = """INSERT INTO usuario (nome, email, cpf_cnpj, senha) VALUES (%s, %s, %s, %s)"""
    values = [nome, email, cpf, senha]
    cursor.execute(statement, values)
    conn.commit()

    def loginUser_mysql(email, password):
        statement = text ("SELECT * FROM Usuario WHERE email = %s AND senha= %s",(email, password)) #esse parenteses aqui está passando os params
        rs = conn.execute(statement)
        usuario = rs.fetchone() 
        print(usuario)
        if usuario == None:
            return None
        # result = [dict(user) for user in usuario]
        return usuario

def criarTabelaTipo(): #que guardará o tipo se é aluno ow professor
    with engine.connect() as con:    
        create_tabela_tipo = """       

        CREATE TABLE IF NOT EXISTS Tipo (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
        """
        con.execute(create_tabela_tipo);

def populaTabelaTipo(dic):
    nome = dic['nome']
    with engine.connect() as con:
        sql_criar = "INSERT INTO Tipo (nome) VALUES (:name_)",
        con.execute(sql_criar, name_=nome)

def inicializaTBTipo():
    populaTabelaTipo({"nome":"Aluno"})
    populaTabelaTipo({"nome":"Professor"})

#criar tabela usuário
def criarTabelaUsuario():
    with engine.connect() as con:    
        create_tabela_usuario = """       

        CREATE TABLE IF NOT EXISTS Usuario (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            user_type INTEGER NOT NULL,
            password TEXT NOT NULL,
            is_active INTEGER NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            FOREIGN KEY (user_type) REFERENCES Tipo (id)
        )
        """
        con.execute(create_tabela_usuario);

def inserirUsuario(usuario):
    nome = usuario['name']
    email = usuario['email']
    aluno = usuario['user_type_id']
    senha = usuario['password']
    ativo = usuario['is_active']
    cpf_cnpj = usuario['cpf_cnpj']
    tel = usuario['phone']
    with engine.connect() as con:    
        sql_criar = """INSERT INTO Usuario (nome, email, cpf, phone, user_type, is_active, password) 
        VALUES (:nome_user, :email_user, :cpf_user, :phone_user, :type_user, :active_user, :pass_user)"""
        con.execute(sql_criar, nome_user=nome, email_user=email, cpf_user=cpf_cnpj,
        phone_user=tel, type_user=aluno, active_user=ativo, pass_user=senha)

def loginUser(email, password):
    with engine.connect() as con:  #conecta no meu banco de dados
        statement = text ("""SELECT * FROM Usuario WHERE email= :email_ AND password= :pass_""") 
        rs = con.execute(statement, email_=email, pass_=password) 
        usuario = rs.fetchone() 
        print(usuario)
        if usuario == None:
            return None
        # result = [dict(user) for user in usuario]
        return usuario
        


def getDisciplinaId(id_disciplina):
    with engine.connect() as con:  #conecta no meu banco de dados
        statement = text ("""SELECT * FROM Disciplina WHERE id= :id_ """) 
        rs = con.execute(statement, id_=id_disciplina) 
        disciplina = rs.fetchone()                   
        if disciplina == None:
            return None
        return dict(disciplina)                        
                                                 


def excluirDisciplina(id_disciplina):
    disciplina = getDisciplinaId(id_disciplina)
    if disciplina == None:
        return None
    with engine.connect() as con:    
        sql = text( """DELETE FROM Disciplina
                    WHERE id = :id_ and NOT EXISTS (
                        SELECT 1 FROM Matricula where
                            Matricula.id_disciplina = Disciplina.id
                        )""")
        con.execute(sql, id_=id_disciplina) 
    return disciplina



def alterarDisciplina(id_disciplina, novos_dados):
    disciplina = getDisciplinaId(id_disciplina)
    if disciplina == None:
        return None

    with engine.connect() as con:    
        sql_editar = "UPDATE Disciplina SET nome=:nome WHERE id =:id_"
        con.execute(sql_editar, nome=novos_dados['nome'], id_=id_disciplina)
    return disciplina

