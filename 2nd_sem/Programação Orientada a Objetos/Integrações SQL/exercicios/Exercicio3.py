'''Exercício 3

Crie as tabelas abaixo no banco de dados SQLITE e faça o mapeamento dessas tabelas utilizando o SQLAlchemy.
Implementar um programa para realizar as seguintes operações:
Cadastrar um médico.
Cadastrar dois pacientes.
Cadastrar dois exames (um para cada paciente).
Inserir os dados cadastrados banco de dados.
Realizar uma consulta no banco de dados para verificar se os dados foram inseridos corretamente.

Scripts para criação das tabelas no banco de dados:
connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")

'''

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///Integrações SQL/exercicios/exercicio3.db")
connection = engine.connect()

session = Session()
Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")

class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(255))
    especializacao = Column('ESPECIALIZACAO',String(255))

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado

medico1 = Medico('Ronaldo', 159685, 'Ortopedista')
session.add(medico1)
session.commit()

paciente1 = Paciente('Romario', 42356589736, 37)
paciente2 = Paciente('Adriano', 42353024858, 42)
pac = [paciente1 , paciente2]
session.add_all(pac)
session.commit()

exame1 = Exame(medico1.id, paciente1.id, 'Acidente de moto', 'Sofreu uma concussão')
exame2 = Exame(medico1.id, paciente2.id, 'Queda de skate', 'Quebrou o tornozelo')
lista = [exame1, exame2]
session.add_all(lista)
session.commit()

# print('-'*30)
# resultado = session.query(Medico)
# for x in resultado:
#     print(x.nome, x.crm, x.especializacao)

# print('-'*30)
# resultado = session.query(Paciente)
# for x in resultado:
#     print(x.nome, x.cpf, x.idade)

# print('-'*30)
# resultado = session.query(Exame)
# for x in resultado:
#     print(x.id_medico, x.id_paciente, x.descricao, x.resultado)


print('-'*30)
resultado = session.query(Medico, Exame, Paciente).filter(Exame.id_medico == Medico.id, Exame.id_paciente == Paciente.id)
for x in resultado:
    print(x.Medico.nome, x.Medico.crm, x.Medico.especializacao, x.Paciente.nome,
    x.Paciente.cpf, x.Paciente.idade, x.Exame.id_paciente, x.Exame.id_medico,
    x.Exame.descricao, x.Exame.resultado)

# print('-'*30)
# resultado = session.query(Paciente, Exame).filter(Exame.id_paciente == Paciente.id)
# for x in resultado:
#     print(x.Paciente.nome, x.Exame.id_paciente)
