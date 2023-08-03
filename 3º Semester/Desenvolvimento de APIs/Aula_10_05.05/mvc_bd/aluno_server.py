from flask import Flask, request

import aluno_model

app = Flask(__name__) 

'''
Arquivo que cria o servidor (rotas) e é o controller
'''

@app.route('/')
def start():
    aluno_model.criarTabelaAluno()
    return "Criando nossa Tabela Alunos no Banco de Dados"

@app.route('/inicializa')
def inicializaTabelaAluno():
    aluno_model.inicializarTabelaAluno()
    return "Alunos inseridos no Banco de Dados"


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
def inserir(): 
    aluno = request.json 
    aluno_model.inserirAluno(aluno) 
    return  getAlunos()
	

@app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def excluir(id_aluno):
    aluno = aluno_model.excluirAluno(id_aluno)
    if aluno == None:
        return 'Aluno não encontrado' 
    return 	getAlunos()


@app.route("/alunos/<int:id_aluno>", methods=["PUT"])	
def alterar(id_aluno): 
    novo_aluno = request.json 
    aluno = aluno_model.alterarAluno(id_aluno, novo_aluno) 
    if aluno == None:
        return 'Aluno não encontrado' 
    return  getAlunos() 	
	


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True) 