from flask import jsonify

from sqlalchemy.sql import text

import conexao_bd

engine = conexao_bd.getConexao()


#criar a tabela Aluno
def criarTabelaAluno():
    with engine.connect() as con:    
        create_tabela_aluno = """
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """    
        con.execute(create_tabela_aluno)

    
def inserirAluno(aluno):
    nome = aluno['nome']
    email = aluno['email']
    with engine.connect() as con:    
        sql_criar = "INSERT INTO Aluno (nome,email) VALUES (:meuNome, :meuEmail)"
        con.execute(sql_criar, meuNome=nome, meuEmail=email)

        # Repare que a minha query nao especificou uma coluna: a ID do aluno
        # o sqlite está preenchendo essa coluna sozinho (como podemos ver na criacao
        #da tabela)

    
def inicializarTabelaAluno():
    inserirAluno({'nome': "Andreia", 'email': "andreia.gusmao@faculdadeimpacta.com.br"})
    inserirAluno({'nome': "Arthur", 'email': "email_arthur@faculdadeimpacta.com.br"})
    inserirAluno({'nome': "Pedro", 'email': "email_pedro@faculdadeimpacta.com.br"})
    inserirAluno({'nome': "Ana", 'email': "email_ana@faculdadeimpacta.com.br"})


                     	
def getAlunos():
    with engine.connect() as con:  #conecta no meu banco de dados
        statement = text ("""SELECT * FROM Aluno""") 
        
        rs = con.execute(statement) 
        alunos = rs.fetchall()                 #pega todos os resultados
        if alunos == []:                       #se nao tinha nenhuma linha
            return None
        result = [dict(aluno) for aluno in alunos]
        return jsonify(result)
        


def getAlunoId(id_aluno):
    with engine.connect() as con:  #conecta no meu banco de dados
        #query com "buraco" com o id do aluno    
        statement = text ("""SELECT * FROM Aluno WHERE id = :id_""") 
        # :id_ -> buraco que vai ser preenchido quando eu chamar con.execute
        
        rs = con.execute(statement, id_=id_aluno) #e usei esse buraco
        aluno = rs.fetchone()                   #pega a primeira linha do resultado
        if aluno == None:
            return None
        return dict(aluno)



def getAlunoNome(nome_aluno):
    with engine.connect() as con:  #conecta no meu banco de dados
        #query com "buraco" com o nome jogador    
        statement = text ("""SELECT * FROM Aluno WHERE nome = :nome_""") 
        # :nome_ -> buraco que vai ser preenchido quando eu chamar con.execute
        
        rs = con.execute(statement, nome_=nome_aluno) #e usei esse buraco
        alunos = []
        while True:
            batch = rs.fetchmany(20)  # obtem 20 alunos por lote
            if not batch:
                break  # finaliza o loop se não houver mais lotes
            for aluno in batch:
                alunos.append(dict(aluno))  # transforma cada linha em um dicionário e adiciona na lista
    return jsonify(alunos)
	

def excluirAluno(id_aluno):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o aluno realmente existe
   
    aluno = getAlunoId(id_aluno)
    if aluno == None:
        return None
    with engine.connect() as con:    
        sql = "DELETE FROM Aluno WHERE id = :id_"
        con.execute(sql, id_=id_aluno) 
    return aluno



def alterarAluno(id_aluno, novos_dados):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o aluno realmente existe
    aluno = getAlunoId(id_aluno)
    if aluno == None:
        return None
    
    with engine.connect() as con:    
        sql_editar = "UPDATE Aluno SET nome=:nome, email=:email WHERE id =:id_"
        con.execute(sql_editar, nome=novos_dados['nome'], 
                    email=novos_dados['email'], id_=id_aluno)
    return aluno

