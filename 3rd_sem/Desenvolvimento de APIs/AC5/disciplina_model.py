from flask import jsonify

from sqlalchemy.sql import text

import conexao_bd

engine = conexao_bd.getConexao()


#criar a tabela Disciplina
def criarTabelaDisciplina():
    with engine.connect() as con:    
        create_tabela_disciplina = """
        CREATE TABLE IF NOT EXISTS Disciplina (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL UNIQUE
        )
        """    
        con.execute(create_tabela_disciplina);

    
def inicializarTabelaDisciplina():
    inserirDisciplina({'nome': "Lógica de Programação"})
    inserirDisciplina({'nome': "Matemática"})
    inserirDisciplina({'nome': "Banco de Dados"})
    inserirDisciplina({'nome': "Desenvimento de Microsserviços e APIs"})


def inserirDisciplina(disciplina):
    nome = disciplina['nome'] 
    with engine.connect() as con:    
        sql_criar = "INSERT INTO Disciplina (nome) VALUES (:nome_disciplina)"
        con.execute(sql_criar, nome_disciplina=nome)

      
def getDisciplinas():
    with engine.connect() as con:  #conecta no meu banco de dados
        statement = text ("""SELECT * FROM Disciplina""") 
        
        rs = con.execute(statement) 
        disciplinas = rs.fetchall()                 
        if disciplinas == []:                       
            return None
        result = [dict(disciplina) for disciplina in disciplinas]
        return jsonify(result)
        


def getDisciplinaId(id_disciplina):
    with engine.connect() as con:  #conecta no meu banco de dados
        statement = text ("""SELECT * FROM Disciplina WHERE id = :id_""") 
        
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

