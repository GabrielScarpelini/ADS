from flask import jsonify

from sqlalchemy.sql import text

import conexao_bd

engine = conexao_bd.getConexao() 

def criaTbPessoa():
    with engine.connect() as con:
        create_tb_pessoa = text("""
        CREATE TABLE IF NOT EXISTS Pessoa (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
        """)
        con.execute(create_tb_pessoa)
    
def criaInteresse():
    with engine.connect() as con:
        create_interesse = text("""
        CREATE TABLE IF NOT EXISTS Interesse (
            id_interessado INTEGER, 
            id_interesse INTEGER,
            PRIMARY KEY(id_interessado, id_interesse),
            FOREIGN KEY (id_interessado) REFERENCES Pessoa(id)
            FOREIGN KEY (id_interesse) REFERENCES Pessoa(id)
        )
        """)
        con.execute(create_interesse)

def inserirPessoa(pessoa):
    nome = pessoa['nome']
    with engine.connect() as con:    
        sql_criar = text("""INSERT INTO Pessoa (nome) VALUES (:pessoaNome)""")
        con.execute(sql_criar, pessoaNome=nome)
        con.commit()

def inicializarTabelaPessoas():
    inserirPessoa({'nome': "Andreia"})
    inserirPessoa({'nome': "Arthur"})
    inserirPessoa({'nome': "Pedro"})
    inserirPessoa({'nome': "Ana"})

database = {}

#um dicion�rio, que tem a chave 'INTERESSES' para o controle
#dos interesses (que pessoa se interessa por que outra), 
#e a chave 'PESSOAS para o controle de pessoas 
# (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)


class NotFoundError(Exception):
    pass
class IncompatibleError (Exception):
    pass

database['PESSOAS'] = [
    {"id": 9, "nome": "Marcos"}, 
    {"id": 3, "nome": "Ana"}, 
    {'nome':'Fernando','id':1},
    {'nome':'Olga','id':10}
]

database['INTERESSES'] = { 
    9: [3,10], 
    1: [3],
    3: [9],
    10: [9,1]
}

def reseta():
    database["PESSOAS"] = []
    database['INTERESSES'] = {}

# Pegar a lista de todas as pessoas : i.todas_as_pessoas()

def todas_as_pessoas():
    return database['PESSOAS']


def localiza_pessoa(id_pessoa): 
    for dic_pessoa in database["PESSOAS"]:
        if dic_pessoa['id'] == id_pessoa:
            return dic_pessoa
    raise NotFoundError



def adiciona_pessoa(dic_pessoa): #{'nome':'','id':}
    database["PESSOAS"].append(dic_pessoa)     #adiciona um dicionario na lista de pessoas
    id_pessoa = dic_pessoa['id']
    database['INTERESSES'][id_pessoa] = []    # cria uma lista vazia na database['INTERESSES']      
                                             


def adiciona_interesse(id_interessado, id_alvo_de_interesse): # 10,3
    localiza_pessoa(id_interessado)
    #d� erro se id_interessado n�o existe na lista de pessoas
    localiza_pessoa(id_alvo_de_interesse)
    lista_interesses = database['INTERESSES'][id_interessado]
    # dic database tem chave interesses, que � dic
    # database['INTERESSES'] tem chave 10, que � lista
    # vou inserir 3 em database['INTERESSES'][10]
    if id_alvo_de_interesse not in  lista_interesses:
        lista_interesses.append(id_alvo_de_interesse)


def consulta_interesses(id_interessado):
    localiza_pessoa(id_interessado)
    return database['INTERESSES'][id_interessado]



def remove_interesse(id_interessado, id_alvo_de_interesse):
    localiza_pessoa(id_interessado)
    localiza_pessoa(id_alvo_de_interesse)
    lista_interesses = database['INTERESSES'][id_interessado]
    if id_alvo_de_interesse in lista_interesses:
        lista_interesses.remove(id_alvo_de_interesse)



#Matches  
# Para toda pessoa que Olga gosta, tenho que verificar se cada uma gosta do Olga
def lista_matches(id_pessoa): 
    localiza_pessoa(id_pessoa)
    lista_interesses = database['INTERESSES'][id_pessoa]
    lista_dos_matches = []
    for id_alvo in lista_interesses:
        lista_interesses_do_alvo = database['INTERESSES'][id_alvo]
        if id_pessoa in lista_interesses_do_alvo: #A pessoa tb gosta do Olga??
           lista_dos_matches.append(id_alvo)
    return lista_dos_matches



