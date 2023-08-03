"""Exercício 1

Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar a tabela FUNCIONARIO (utilize o script abaixo para a criação da tabela).
Criar uma classe Funcionario e mapear a tabela criada anteriormente.
Instanciar três objetos da classe Funcionario.
Inserir os dados dos objetos na tabela. 
Realizar uma consulta na tabela de funcionários e verificar se os dados foram inseridos corretamente.
Realizar uma consulta na tabela de todos os funcionários com salário superior a R$ 1.500,00.

Scripts para criação das tabelas no banco de dados:
connection.execute(CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///Integrações SQL/exercicios/exercicio1.db")
connection = engine.connect()

session = Session()
Base = declarative_base(engine)


connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")

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

func1 = Funcionario(111,'zeka', 19, 1250)
func2 = Funcionario(222,'Daniel', 25, 2500)
func3 = Funcionario(333,'Igor', 20, 1300)
lista = [func1, func2, func3]
session.add_all(lista)
session.commit

print('-'*30)
resultado = session.query(Funcionario)
for obj in resultado:
    print(obj.nome, obj.idade, obj.salario)

print('-'*30)
resultado = session.query(Funcionario).filter(Funcionario.salario > 1500)
for obj in resultado:
    print(obj.nome, obj.idade, obj.salario)
