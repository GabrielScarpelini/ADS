from flask import jsonify

from sqlalchemy.sql import text

import conexao_bd

engine = conexao_bd.getConexao()

#criar tabela usuário
def criarTabelaUsuario():
    with engine.connect() as con:    
        create_tabela_usuario = """
        CREATE TABLE IF NOT EXISTS Usuario (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            bday DATE NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            user_type INTEGER NOT NULL,
            is_active INTEGER NOT NULL,
            terms INTEGER NOT NULL,
            password TEXT NOT NULL
        )
        """
        con.execute(create_tabela_usuario);

def inserirUsuario(usuario):
    nome = usuario['name']
    email = usuario['email']
    aluno = usuario['user_type_id']
    senha = usuario['password']
    ativo = usuario['is_active']
    termos = usuario['terms']
    niver = usuario['birthday']
    tel = usuario['phone']
    cpf_cnpj = usuario['cpf_cnpj']
    with engine.connect() as con:    
        sql_criar = """INSERT INTO Usuario (nome, email, bday, cpf, phone, user_type, is_active, terms, password) 
        VALUES (:nome_user, :email_user, :bday_user, :cpf_user, :phone_user, :type_user, :active_user, :terms_user,
        :pass_user)"""
        con.execute(sql_criar, nome_user=nome, email_user=email, bday_user=niver, cpf_user=cpf_cnpj,
        phone_user=tel, type_user=aluno, active_user=ativo, terms_user=termos, pass_user=senha)

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

