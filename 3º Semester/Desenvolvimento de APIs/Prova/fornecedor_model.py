from flask import jsonify

from sqlalchemy.sql import text

from sqlalchemy import create_engine

engine = create_engine('sqlite:///prova.db') 
    

#criar a tabela Fornecedor
def criarTabelaFornecedor():
    with engine.connect() as con:
        sql = text("""
        CREATE TABLE IF NOT EXISTS Fornecedor (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cnpj TEXT NOT NULL UNIQUE
        )
        """)
        con.execute(sql);


#1)Crie a função para inserir um novo fornecedor
def inserirFornecedor(fornecedor):
    with engine.connect() as con:
        statement = text("""INSERT INTO Fornecedor (nome, cnpj) VALUES (:nomeForn, :cnpjForn)""")
        con.execute(statement, nomeForn=fornecedor['nome'], cnpjForn=fornecedor["cnpj"])


#Função para pesquisar todos os fornecedores cadastrados
def getFornecedores():
    with engine.connect() as con:
        statement = text ("""SELECT * FROM Fornecedor""") 
        rs = con.execute(statement) 
        fornecedores = rs.fetchall()
        if fornecedores == []:
            return None
        result = [dict(fornecedor) for fornecedor in fornecedores]
        return jsonify(result)
	

#2)Crie a função para pesquisar o fornecedor pelo seu id
def getFornecedorId(id_fornecedor):
    with engine.connect() as con:  
        statement = text ("""SELECT * FROM Fornecedor WHERE id = :id_""")
        rs = con.execute(statement, id_=id_fornecedor)
        fornecedor = rs.fetchone()
        return dict(fornecedor)


#3)Crie a função para excluir um fornecedor pelo id, se ele existir
def excluirFornecedor(id_fornecedor):
    with engine.connect() as con:  
        statement = text ("""DELETE FROM Fornecedor WHERE id = :id_""")
        rs = con.execute(statement, id_=id_fornecedor)
        return True


#4)Crie a função para alterar um forneedor pelo id, se ele existir
def alterarFornecedor(id_fornecedor, novos_dados):
    with engine.connect() as con:
        statement = text ("""UPDATE Fornecedor SET nome=:nome_, cnpj=:cnpj_ WHERE id =:id_""")
        rs = con.execute(statement, nome_=novos_dados["nome"], cnpj_=novos_dados["cnpj"], id_=id_fornecedor)
        return True