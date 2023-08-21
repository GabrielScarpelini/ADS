'''Crie a tabela abaixo no banco de dados SQLITE e faça o mapeamento dessa
   tabela utilizando o SQLAlchemy.
   
Considere um arquivo de texto contendo os dados dos funcionários de uma empresa. Cada linha do arquivo contém as informações sobre um funcionário, no formato: nome;idade;salario

Implementar um programa para realizar as seguintes operações:
Abrir e ler o conteúdo do arquivo de texto.
Inserir os dados do arquivo de texto na tabela do banco de dados.
Realizar consultas no banco de dados e exibir os dados no terminal.

Exemplo de arquivo de texto com os dados dos funcionários:
'''

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///Integrações SQL/Exercício_2/exercicio1.db")
connection = engine.connect()

session = Session()
Base = declarative_base(engine)

arquivo = open('Integrações SQL/Exercício_2/arquivo.txt', 'r', encoding="UTF-8")

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")

class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer,primary_key=True, autoincrement=True)
    nome = Column('NOME',String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self,nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

emp = []

for linha in arquivo:
    lista = linha.split(';')
    func = Funcionario(lista[0], lista[1], lista[2])
    emp.append(func)

session.add_all(emp)
session.commit()
    

var = session.query(Funcionario).order_by(Funcionario.nome)

for x in var:
    print(x.nome, x.idade, x.salario)