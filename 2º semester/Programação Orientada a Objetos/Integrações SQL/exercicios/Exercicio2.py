"""Exercício 2

Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar as tabelas AUTOR e LIVRO (utilize os scripts abaixo para a criação das tabelas).
Criar as classes Autor e Livro e fazer o mapeamento das tabelas.
Inserir nas tabelas dois autores e dois livros.
Fazer uma consulta para verificar se os dados foram inseridos corretamente. 

Scripts para criação das tabelas no banco de dados:
connection.execute(CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)

connection.execute("""

'''CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL))'''

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///Integrações SQL/exercicios/exercicio2.db")
connection = engine.connect()

session = Session()
Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")

class Autor(Base):
    __tablename__ = 'AUTOR'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome 

class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas 
        self.autor_id = autor_id

autor1 = Autor('Carinha que mora logo aí')
autor2 = Autor('Daniel o fumador de rowlas')
lista = [autor1, autor2]
session.add_all(lista)
session.commit()

livro1 = Livro('Percy jackson', 297, autor1.id)
livro2 = Livro('Lago, O Elon Musk', 359, autor2.id)
lista = [livro1, livro2]
session.add_all(lista)
session.commit()

print('-'*30)
resultado = session.query(Livro, Autor).filter(Livro.autor_id == Autor.id)
for x in resultado:
    print(x.Livro.titulo, x.Autor.id)



