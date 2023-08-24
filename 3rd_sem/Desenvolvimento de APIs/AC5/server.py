from flask import Flask, request
from flask import jsonify

import aluno_model
import disciplina_model
import matricula_model

app = Flask(__name__) 

'''
Arquivo que cria o servidor (rotas) e é o controller
'''

@app.route('/')
def start():
    aluno_model.criarTabelaAluno()
    disciplina_model.criarTabelaDisciplina()
    matricula_model.criarTabelaMatricula()
    return "Criando as Tabelas no Banco de Dados"

@app.route('/inicializa')
def inicializaTabelas():
    aluno_model.inicializarTabelaAluno()
    disciplina_model.inicializarTabelaDisciplina()
    return "Alunos e disciplinas inseridos no Banco de Dados"


#############################################################################
#Alunos
##############################################################################


@app.route('/alunos')
def getAlunos():
    alunos = aluno_model.getAlunos() 
    if alunos == None: 
        return 'Não existem alunos cadastrados. Verifique!' 
    return alunos

@app.route("/alunos/<int:id_aluno>", methods=["GET"])
def getAlunoId(id_aluno): 
    aluno = aluno_model.getAlunoId(id_aluno) 
    if aluno == None: 
        return 'Aluno não encontrado' 
    return 	aluno

@app.route("/alunos/<nome_aluno>", methods=["GET"])
def getAlunoNome(nome_aluno):
    aluno = aluno_model.getAlunoNome(nome_aluno) 
    if aluno == None: 
        return 'Aluno não encontrado' 
    return 	aluno

     
@app.route("/alunos", methods=["POST"])	
def inserirAluno(): 
    aluno = request.json 
    aluno_model.inserirAluno(aluno) 
    return  getAlunos()
	

@app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def excluirAluno(id_aluno):
    aluno = aluno_model.excluirAluno(id_aluno)
    if aluno == None:
        return 'Aluno não encontrado' 
    return 	getAlunos()


@app.route("/alunos/<int:id_aluno>", methods=["PUT"])	
def alterarAluno(id_aluno): 
    novo_aluno = request.json 
    aluno = aluno_model.alterarAluno(id_aluno, novo_aluno) 
    if aluno == None:
        return 'Aluno não encontrado' 
    return  getAlunos() 	
	
##########################################################################
#Disciplina
##########################################################################


@app.route('/disciplinas')
def getDisciplinas():
    disciplinas = disciplina_model.getDisciplinas() 
    if disciplinas == None: 
        return 'Não existem disciplinas cadastradas. Verifique!' 
    return disciplinas

@app.route("/disciplinas/<int:id_disciplina>", methods=["GET"])
def getDisciplinaId(id_disciplina): 
    disciplina = disciplina_model.getDisciplinaId(id_disciplina) 
    if disciplina == None: 
        return 'Disciplina não encontrado' 
    return 	disciplina

@app.route("/disciplinas/<nome_disciplina>", methods=["GET"])
def getDisciplinaNome(nome_disciplina):
    disciplina = disciplina_model.getDisciplinaNome(nome_disciplina) 
    if disciplina == None: 
        return 'Disciplina não encontrada' 
    return 	disciplina

     
@app.route("/disciplinas", methods=["POST"])	
def inserirDisciplina(): 
    disciplina = request.json 
    disciplina_model.inserirDisciplina(disciplina) 
    return  getDisciplinas()
	

@app.route("/disciplinas/<int:id_disciplina>", methods=["DELETE"])
def excluirDisciplina(id_disciplina):
    disciplina = disciplina_model.excluirDisciplina(id_disciplina)
    if disciplina == None:
        return 'Disciplina não encontrada' 
    return 	getDisciplinas()


@app.route("/disciplinas/<int:id_disciplina>", methods=["PUT"])	
def alterarDisciplina(id_disciplina): 
    novo_disciplina = request.json 
    disciplina = disciplina_model.alterarDisciplina(id_disciplina, novo_disciplina) 
    if disciplina == None:
        return 'Disciplina não encontrada' 
    return  getDisciplinas() 	
	
##########################################################################
#Matrícula do Aluno em Disciplinas
##########################################################################


@app.route("/matriculas/aluno/<int:id_aluno>", methods=["GET"])
def getMatriculaIdAluno(id_aluno): 
    disciplinas = matricula_model.getMatriculasIdAluno(id_aluno) 
    if disciplinas == False: 
        return 'Aluno não existe' 
    
    if disciplinas == None: 
        return 'Aluno não está matriculado em nenhuma disciplina' 
    return 	disciplinas


@app.route("/matriculas/disciplina/<int:id_disciplina>", methods=["GET"])
def getMatriculaIdDisciplina(id_disciplina): 
    alunos = matricula_model.getMatriculasIdDisciplina(id_disciplina) 
    if alunos == False: 
        return 'Disciplina não existe' 
    if alunos == None: 
        return 'Disciplina não tem nenhum aluno matriculado' 
    
    return 	alunos

     
@app.route("/matriculas", methods=["POST"])
def matriculas(): 
    matricula = request.json 
    result = matricula_model.matricular(matricula) 
    if result == False: 
        return 'Aluno e/ou Disciplina não existe(m). Verifique.' 
    
    if result == None:
        return 'Matrícula já existe'
    return jsonify({"status":"ok"})
	

@app.route("/matriculas/<int:id_aluno>/<int:id_disciplina>", methods=["DELETE"])
def excluirMatricula(id_aluno, id_disciplina):
    result = matricula_model.excluirMatricula(id_aluno, id_disciplina)
    if result == False: 
        return 'Aluno e/ou Disciplina não existe(m). Verifique.' 
    
    if result == None:
        return 'Matrícula não existe'
    return 	jsonify({"status":"ok"})


###############################################################################

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)