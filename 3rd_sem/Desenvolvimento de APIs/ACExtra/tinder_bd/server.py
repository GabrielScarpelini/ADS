from flask import Flask, jsonify, request 
import estrutura_interesses as i

app = Flask(__name__) 

@app.route('/')
def start():
    i.criaTbPessoa()
    i.criaInteresse()
    return "Criando as Tabelas no Banco de Dados"

@app.route('/inicializa')
def startTable():
    i.inicializarTabelaPessoas()
    return f'Pessoas inseridas com sucesso'                                  

# /pessoas, com GET, para pegar a lista de todas as pessoas

@app.route("/pessoas", methods=["GET"])
def todas_as_pessoas():
    lista = i.todas_as_pessoas()
    return jsonify(lista)

# /pessoas, com POST, receber um dicionário de uma pessoa e colocar na lista
@app.route("/pessoas", methods=["POST"])
def add_pessoa():
    #receber um dicionário através do flask?

    # O usuário me mandou alguma coisa, eu acho que foi um json
    # quero que voce transforme num dicionário pra mim
    dic_usuario_enviou = request.json
    i.adiciona_pessoa(dic_usuario_enviou)
    return jsonify({"status":"ok"})

# /pessoas/id_pessoa, com GET, para localizar no dicionario da pessoa pelo id
@app.route('/pessoas/<int:id_pessoa>', methods=["GET"])
def localiza_pessoa(id_pessoa):
    pessoa = i.localiza_pessoa(id_pessoa)
    return jsonify(pessoa)


# adiciona_interesse (id_interessado, id_alvo_de_interesse): # 10,3
@app.route("/pessoas/interesse/<int:id_interessado>/<int:id_alvo_de_interesse>", methods=['POST'])
def add_interesse(id_interessado, id_alvo_de_interesse):
    i.adiciona_interesse(id_interessado, id_alvo_de_interesse)
    return jsonify({"status":"ok"})
    


# /pessoas/interesse, com GET
@app.route("/pessoas/interesse/<int:id_pessoa>", methods=['GET'])
def get_interesses(id_pessoa):
    interesses = i.consulta_interesses(id_pessoa)
    return jsonify(interesses)


# /pessoas/interesse, com DELETE 
@app.route("/pessoas/interesse/<int:id_interessado>/<int:id_alvo_de_interesse>", methods=['DELETE'])
def remove_interesse(id_interessado, id_alvo_de_interesse):
    i.remove_interesse(id_interessado, id_alvo_de_interesse)
    return jsonify({"status":"ok"})


# /pessoas/matches, com GET
@app.route("/pessoas/matches/<int:id_pessoa>", methods=['GET'])
def get_matches(id_pessoa):
    matches =  i.lista_matches(id_pessoa)  
    return jsonify(matches)

# /reseta, com POST, para esvaziar a lista de pessoas
@app.route("/reseta", methods=["POST"])
def reseta():
    i.reseta()
    return jsonify({"status":"ok"})
    
if __name__ == '__main__':         #rodar o servidor
   app.run(host = 'localhost', port = 5002, debug = True)