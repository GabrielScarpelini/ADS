from flask import Flask, request

import fornecedor_model

app = Flask(__name__) 

'''
Arquivo que cria o servidor (rotas) e é o controller
'''

#rota padrão
@app.route('/')
def start():
    fornecedor_model.criarTabelaFornecedor()
    return "Criando a Tabela no Banco de Dados"



#rota para mostrar todos os fornecedores cadastrados
@app.route('/fornecedores')
def getFornecedores():
    fornecedores = fornecedor_model.getFornecedores() 
    if fornecedores == None: 
        return 'Não existem fornecedores cadastrados. Verifique!'
    return fornecedores



#1)Crie a rota para pesquisar o fornecedor pelo seu id
@app.route("/fornecedor/<int:id_forn>", methods=["GET"])
def getFornecedorId(id_forn):
    fornecedor = fornecedor_model.getFornecedorId(id_forn) 
    if fornecedor == None: 
        return 'Fornecedor não encontrado'
    return fornecedor

 
#2)Crie a rota para inserir um novo fornecedor
@app.route("/fornecedor", methods=["POST"])	
def inserirFornecedor(): 
    fornecedor = request.json 
    fornecedor_model.inserirFornecedor(fornecedor) 
    return  getFornecedores()
	

#3)Crie a rota para excluir um fornecedor pelo seu id   
@app.route("/fornecedor/<int:id_forn>", methods=["DELETE"])
def excluirFornecedor(id_forn):
    fornecedor = fornecedor_model.excluirFornecedor(id_forn)
    if fornecedor == None:
        return 'Fornecedor não encontrado' 
    return getFornecedores()



#4)Crie a rota para alterar um fornecedor pelo seu id   
@app.route("/fornecedor/<int:id_forn>", methods=["PUT"])	
def alterarFornecedor(id_forn): 
    novo_fornecedor = request.json 
    fornecedor = fornecedor_model.alterarFornecedor(id_forn, novo_fornecedor) 
    if fornecedor == None:
        return 'Fornecedor não encontrado' 
    return  getFornecedores()
	


###############################################################################

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True) 