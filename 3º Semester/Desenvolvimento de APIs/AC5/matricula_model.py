from flask import jsonify

from sqlalchemy.sql import text

import aluno_model
import disciplina_model
import conexao_bd

engine = conexao_bd.getConexao() 


#criar a tabela Matricula
def criarTabelaMatricula():
    with engine.connect() as con:    
        create_tabela_matricula = """
        CREATE TABLE IF NOT EXISTS Matricula (
            id_aluno INTEGER,
            id_disciplina INTEGER,
            PRIMARY KEY (id_aluno, id_disciplina),
            FOREIGN KEY (id_aluno) REFERENCES Aluno (id),
            FOREIGN KEY (id_disciplina) REFERENCES Disciplina (id)
            )
        """    
        con.execute(create_tabela_matricula);

'''
1)Crie uma função que recebe dois parãmetros id_aluno e
    id_disciplina e verifica na tabela Matricula se existe
    esse registro. Se não existir retorna None e se existir, retorna
    a dict(matricula). Essa função será chamada nas funções: matricular e
    excluirMatricula
'''     
def getMatriculaIdAlunoIdDisciplina(id_aluno, id_disciplina):
    with engine.connect() as con:
        statement =  text('''SELECT * FROM Matricula WHERE id_aluno = :id_a_ AND id_disciplina = :id_m_''')
        rs = con.execute(statement, id_a_= id_aluno, id_m_= id_disciplina)
        matricula = rs.fetchone()
        if matricula == None:
            return None

        return dict(matricula)
    
# print(getMatriculaIdAlunoIdDisciplina(1,1))


'''
2)Crie uma função que recebe um dicionário 'matricula' com as chaves id_aluno
    e id_disciplina para salvar na tabela Matricula.
    Se o aluno não existir cadastrado, retorna False
    Se a disciplina não existir cadastrada, retorna False
    Caso ambos existem, então devemos verificar na Tabela de Matriculas
    se o id_aluno e id_matricula já existem na tabela, pois não pode
    existir o mesmo aluno para a mesma disciplina. Nesse caso deve retornar None
    Se não existir, então deve salvar na tabela Matricula e retorna True
'''   
def matricular(matricula): #Matricula = Dicionário
    id_aluno = matricula['id_aluno']
    id_disciplina= matricula['id_disciplina']
    with engine.connect() as con:
        if aluno_model.getAlunoId(id_aluno) == None:
            return False
        else:
            if disciplina_model.getDisciplinaId(id_disciplina) == None:
                return False
            else:
                if getMatriculaIdAlunoIdDisciplina(id_aluno, id_disciplina) == None:
                    statement = ('''INSERT INTO Matricula (id_aluno, id_disciplina) VALUES (:id_aluno_, :id_disciplina_)''')
                    con.execute(statement, id_aluno_ = id_aluno, id_disciplina_= id_disciplina)
                    return True
    return None

'''
3)Crie uma função que recebe o parâmetro id_aluno, verifica se esse
    aluno existe na tabela Aluno (aluno_model.xxxxxxx). Se retornar None,
    retorna então False. Caso contrário, faça a consulta que retorna todas
    as matrículas do aluno id_aluno
'''                       	
def getMatriculasIdAluno(id_aluno):
        if aluno_model.getAlunoId(id_aluno) == None:
            return False
        
        with engine.connect() as con:
            statement = ('''SELECT * FROM Matricula WHERE id_aluno =:id_aluno_''')
            rs = con.execute(statement, id_aluno_ = id_aluno)
            matriculado = rs.fetchall()
            if matriculado == []:
                return None
            result = [dict(matricula) for matricula in matriculado]
            return jsonify(result)

'''
4)Crie uma função que recebe o parâmetro id_disciplina, verifica se essa
    disciplina existe na tabela Disciplina (disciplina_model.xxxxxxx). Se retornar None,
    retorna então False. Caso contrário, faça a consulta que retorna todas
    as matrículas da disciplina id_disciplina
'''   
def getMatriculasIdDisciplina(id_disciplina):
    with engine.connect() as con:
        param = disciplina_model.getDisciplinaId(id_disciplina)
        if param != None:
            statement = ('''SELECT * FROM Matricula WHERE id_disciplina = :id_disciplina_''')
            rs = con.execute(statement, id_disciplina_ = id_disciplina)
            matriculas = rs.fetchall()
            return dict(matriculas)
        else:
            return False



'''
5)Crie uma função que recebe dois paramêtros: id_aluno e id_disciplina.
    Verifica se esse aluno existe na tabela Aluno (aluno_model.xxxxxxx). 
    Se retornar None então retorne False.    
    Verifica se essa disciplina existe na tabela Disciplina (disciplina_model.xxxxxxx). 
    Se retornar None então retorne False.
    Caso ambos existem, então devemos verificar na Tabela de Matriculas
    se o id_aluno e id_matricula já existem na tabela, pois não podemos excluir uma 
    matrícula que não que exista. Nesse caso, se não existir, retorna None
    Caso contrário, exclua da tabela Matricula o registro que tenha os valores
    informados no parâmetro e retorna True
'''   
def excluirMatricula(id_aluno, id_disciplina):
    with engine.connect() as con:
        if aluno_model.getAlunoId(id_aluno) == None:
            return False
        else:
            if disciplina_model.getDisciplinaId(id_disciplina) == None:
                return False
            else:
                if getMatriculaIdAlunoIdDisciplina(id_aluno, id_disciplina) == None:
                    return None
                else:
                    statement = ('''DELETE FROM Matricula WHERE id_disciplina = :id_disciplina_ AND id_aluno = :id_aluno_''')
                    con.execute(statement, id_disciplina_ = id_disciplina, id_aluno_ = id_aluno)
               
    return True




