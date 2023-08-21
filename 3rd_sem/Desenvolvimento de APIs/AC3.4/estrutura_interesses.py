
#esse arquivo � o MODEL

database = {}

#um dicion�rio, que tem a chave 'INTERESSES' para o controle
#dos interesses (que pessoa se interessa por que outra), 
#e a chave 'PESSOAS para o controle de pessoas 
# (quem sao as pessoas e quais sao os dados pessoais de cada pessoa no sistema)


class NotFoundError(Exception):
    pass
class IncompatibleError (Exception):
    pass
class SameIDs(Exception):
    pass
lista = []

database['PESSOAS'] = [
    {"id": 9, "nome": "Marcos"}, 
    {"id": 3, "nome": "Ana"}, 
    {'nome':'Fernando','id':1},
    {'nome':'Olga','id':10}
]

database['INTERESSES'] = { 
    9: [3,10], 
    1: [3],
    3: [9], 
    10: [9,1] 
}

def reseta():
    database["PESSOAS"] = []
    database['INTERESSES'] = {}


def todas_as_pessoas():
    return database['PESSOAS']


def localiza_pessoa(id_pessoa): 
    for pessoa in database['PESSOAS']:
        if pessoa['id'] == id_pessoa:
            return pessoa
    raise NotFoundError




def adiciona_pessoa(dic_pessoa): #{'nome':'','id':}
    dif = True
    for i in range(len(database['PESSOAS'])):
        if dic_pessoa['id'] == database['PESSOAS'][i]['id']:
            dif = False
    if dif == True:
        database['PESSOAS'].append(dic_pessoa)
        database['INTERESSES'][dic_pessoa['id']] = []
        return database
    else:
        raise SameIDs

    #adiciona um dicionario na lista de pessoas
    # cria uma lista vazia na database['INTERESSES'] para o id_pessoa do dic_pessoa


def adiciona_interesse(id_interessado, id_alvo_de_interesse): # 10,3
    for pessoa in database['PESSOAS']:
        if pessoa['id'] == id_interessado:
            for interesse in database['PESSOAS']:
                if interesse['id'] == id_alvo_de_interesse:
                    database['INTERESSES'][id_interessado].append(id_alvo_de_interesse)
                    return database
            raise NotFoundError
    raise NotFoundError
    #d� erro se id_interessado n�o existe na lista de pessoas: tem que localizar a pessoa
    #d� erro se id_alvo_de_interesse n�o existe na lista de pessoas: tem que localizar a pessoa
    # antes de adicionar um interesse, verificar se n�o existe para a pessoa



def consulta_interesses(id_interessado):
    for pessoa in database['PESSOAS']:
        if pessoa['id'] == id_interessado:
            return database['INTERESSES'][id_interessado]
    raise NotFoundError    
    #d� erro se id_interessado n�o existe na lista de pessoas: tem que localizar a pessoa



def remove_interesse(id_interessado, id_alvo_de_interesse):
    for pessoa in database['PESSOAS']:
        if pessoa['id'] == id_interessado:
            for i in range(len(database['INTERESSES'][id_interessado])):
                # breakpoint()
                if database['INTERESSES'][id_interessado][i] == id_alvo_de_interesse:
                   database['INTERESSES'][id_interessado].pop(i)
                   return database
    raise NotFoundError
            
    #d� erro se id_interessado n�o existe na lista de pessoas: tem que localizar a pessoa
    #d� erro se id_alvo_de_interesse n�o existe na lista de pessoas: tem que localizar a pessoa
    # antes de remover um interesse, verificar se j� existe para a pessoa
    return


#Matches  
# Para toda pessoa que Olga gosta, tenho que verificar se cada uma gosta do Olga
# A lista deve retornar todos os interesses de uma pessoa, que se interessa por ela tbem
def lista_matches(id_pessoa): 
    matches_list = []
    if id_pessoa in database['INTERESSES']:
        for pessoa in database['INTERESSES'][id_pessoa]:
            if id_pessoa in database['INTERESSES'][pessoa]:
                matches_list.append(pessoa)
    else:
        raise NotFoundError
    return matches_list

# retornar uma lista mesmo se for só uma pessoa



