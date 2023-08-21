from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///Integrações SQL/Exercício_2/exercicio1.db")
connection = engine.connect()

session = Session()
Base = declarative_base(engine)

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

arquivo = open('Integrações SQL/Exercício_2/nova_lista.txt', 'a', encoding="UTF-8")

sessao = session.query(Funcionario).order_by(Funcionario.nome)

for x in sessao:
    arquivo.write(str(x.nome)+';')
    arquivo.write(str(x.idade)+';')
    arquivo.write(str(x.salario) +'\n')

arquivo.close()