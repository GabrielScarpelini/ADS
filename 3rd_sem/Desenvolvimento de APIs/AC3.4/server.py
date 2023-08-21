from flask import Flask, jsonify, request 
import estrutura_interesses as i

app = Flask(__name__)              
     
#Esse arquivo é o CONTROLLER                              

# /pessoas, com GET, para pegar a lista de todas as pessoas
@app.route("/pessoas", methods=["GET"]) #ok
def pessoas():
    lista = i.todas_as_pessoas()
    return jsonify(lista)

# /pessoas, com POST, receber um dicionário de uma pessoa e colocar na lista só aqui vai usar o corpo de requisição.
@app.route("/pessoas", methods=["POST"])  #ok
def add_pessoa():
    #receber um dicionário através do flask?
    # O usuário me mandou alguma coisa, eu acho que foi um json
    # quero que voce transforme num dicionário pra mim
    dic_usuario_enviou = request.json
    i.adiciona_pessoa(dic_usuario_enviou)
    return jsonify({"status":"ok", "esse cara entrou": dic_usuario_enviou})

@app.route("/")
def helloWord():
    return "Hello World"

# /pessoas/id_pessoa, com GET, para localizar no dicionario da pessoa pelo id
@app.route("/pessoas/<int:id_pessoa>", methods=["GET"]) #ok
def localizar(id_pessoa):
    return jsonify(i.localiza_pessoa(id_pessoa))

@app.route("/pessoas/interesse/<int:id_interessado>/<int:id_alvo_de_interesse>", methods=["POST"]) #ok
def adiciona_interesse(id_interessado, id_alvo_de_interesse): 
    return jsonify(i.adiciona_interesse(id_interessado, id_alvo_de_interesse))


@app.route("/pessoas/interesse/<int:id_interessado>", methods=["GET"]) #ok
def consulta_interesses(id_interessado):
    return jsonify(i.consulta_interesses(id_interessado))

@app.route("/pessoas/interesse/<int:id_interessado>/<int:id_alvo_de_interesse>",  methods=["DELETE"]) #ok
def remove_interesse(id_interessado, id_alvo_de_interesse):
    return jsonify(i.remove_interesse(id_interessado, id_alvo_de_interesse))

@app.route("/pessoas/matches/<int:id_pessoa>", methods=["GET"])  #ok
def lista_matches(id_pessoa): 
    lista = i.lista_matches(id_pessoa)
    return jsonify(lista)

# /reseta, com POST, para esvaziar a lista de pessoas
@app.route("/reseta", methods=["POST"])
def reseta():
    i.reseta()
    return jsonify({"status":"ok"})
    
if __name__ == '__main__':         #rodar o servidor
   app.run(host = 'localhost', port = 5002, debug = True)