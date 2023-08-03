# ATIVIDADE CONTÍNUA 05

# NOMES DOS ALUNOS: (MÁXIMO 8):
# ALUNO 1: nome
# ALUNO 2: nome
# ALUNO 3: nome
# ALUNO 4: nome
# ALUNO 5: nome
# ALUNO 6: nome
# ALUNO 7: nome
# ALUNO 8: nome


# IMPORTAR MÓDULOS
from sqlalchemy import column, create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# CONFIGURAR CONEXÃO COM BANCO DE DADOS SQLITE
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

# INICIAR SESSÃO COM BANCO DE DADOS
session = Session()

# INSTANCIAR CLASSE BASE DO SQLALCHEMY
Base = declarative_base(engine)


# Cria a tabela FILME no banco de dados
connection.execute('''CREATE TABLE IF NOT EXISTS FILME(
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255),
                        DURACAO INT,
                        ANO INT,
                        DIRETOR VARCHAR(255),
                        PAIS VARCHAR(255),
                        NOTA FLOAT)''')




# Implementar classe Filme e realizar o mapeamento da tabela
class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID',Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO',String(255))
    duracao = Column('DURACAO', Integer)
    ano = Column('ANO', Integer)
    diretor = Column('DIRETOR',String(255))
    pais = Column('PAIS',String(255))
    nota = Column('NOTA',Float)

    def __init__(self, titulo, duracao, ano, diretor, pais, nota):
        self.titulo = titulo
        self.duracao = duracao
        self.ano = ano 
        self.diretor = diretor
        self.pais = pais
        self.nota = nota 

# Importar filmes do arquivo movies.txt e inserir no banco de dados
arquivo = open('AC5/movies.txt','r',encoding='UTF-8')
movies = []

for x in arquivo:
    var = x.split(';')
    filme = Filme(var[0], var[1], var[2], var[3], var[4], var[5])
    movies.append(filme)
session.add_all(movies)
session.commit()
print(f'você adicionou {len(movies)} filmes!')
arquivo.close()
# Consultar todos os filmes e ordenar pelo ano de lançamento

sessao = session.query(Filme).order_by(Filme.ano)
for x in sessao:
    print(x.titulo, x.ano)

# Consultar filmes do ano de 2020 e ordenar pelo título

sessao = session.query(Filme).filter(Filme.ano == 2020).order_by(Filme.titulo)
for x in sessao:
    print(x.titulo, x.ano)


# Consultar todos os filmes do país "Brazil" e ordenar pelo título

sessao = session.query(Filme).filter(Filme.pais == 'Brazil').order_by(Filme.titulo)
for x in sessao:
     print(x.titulo, x.ano, x.pais)

# Consultar filme com a melhor nota

sessao = session.query(Filme).order_by(Filme.nota.desc()).limit(1)
for x in sessao:
    print(x.titulo, x.ano, x.nota)

# Excluir do banco de dados todos os filmes do ano de 2018

sessao = session.query(Filme).filter(Filme.ano == 2018)
for x in sessao:
    session.delete(x)
ses = session.query(Filme).filter(Filme.ano == 2018)
for x in ses:
    print(x.titulo, x.ano)
if ses:
    print('sim')
else:
    print('não')


# Exportar filmes para um arquivo de texto, ordenados pelo título e no formato:
file = open('AC5/resultado.txt', 'w', encoding='UTF-8')
sessao = session.query(Filme).order_by(Filme.titulo)
for x in sessao:
    arq = f'{x.id};{x.titulo};{x.duracao};{x.ano};{x.diretor};{x.pais};{x.nota}\n'
    file.write(arq)
file.close()
# id;título;duraçao;ano;diretor;país;nota
session.close()