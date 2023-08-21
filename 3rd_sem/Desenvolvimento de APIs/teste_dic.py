class NotFoundError(Exception):
    pass
class IncompatibleError (Exception):
    pass

dic = {}

dic['PESSOAS'] = [
    {'id': 6, 'nome': 'Juliane Lopes Tomaz'},
    {'id': 3, 'nome': 'Gabriel Scarpelini Pavia'},
    {'id': 10, 'nome': 'Neusa Lopes Tomaz'},
    {'id': 11, 'nome': 'Antonio Carlos Tomaz (baiano)'},
    {'id': 12, 'nome': 'Cristina Scarpelini Pavia'},
    {'id': 13, 'nome': 'Antonio Carlos Pavia'},

]

dic['MATCHS'] = {
    3: [6, 10, 12],
    6: [11, 13],
    10: [11, 6],
    11: [10, 6],
    12: [10, 11],
    13: [3, 6, 10],
     
}

def adiciona_pessoa(dic_pessoa): #{'nome':'','id':}
    dic['PESSOAS'].append(dic_pessoa)
    dic['MATCHS'][dic_pessoa['id']] = []
    return dic

def adiciona_interesse(id_interessado, id_alvo_de_interesse): # 10,3
    for pessoa in dic['PESSOAS']:
        if pessoa['id'] == id_interessado:
            for interesse in dic['PESSOAS']:
                if interesse['id'] == id_alvo_de_interesse:
                    return dic['MATCHS'][id_interessado].append(id_alvo_de_interesse)
            raise NotFoundError
        else: 
            raise NotFoundError

def localiza_pessoa(id_pessoa):
    for pessoa in dic['PESSOAS']:
        if pessoa['id'] == id_pessoa:
            return pessoa
    raise NotFoundError

def remove_interesse(id_interessado, id_alvo_de_interesse):
    for pessoa in dic['PESSOAS']:
        if pessoa['id'] == id_interessado:
            for i in range(len(dic['MATCHS'][id_interessado])):
                # breakpoint()
                if dic['MATCHS'][id_interessado][i] == id_alvo_de_interesse:
                   dic['MATCHS'][id_interessado].pop(i)
                   return dic
    raise NotFoundError

def lista_matches(id_pessoa): 
    matches_list = []
    for pessoa in dic['MATCHS'][id_pessoa]:
        if id_pessoa in dic['MATCHS'][pessoa]:
            matches_list.append(pessoa)
    return matches_list


print(lista_matches(3))
# adiciona_pessoa({'id': 69, 'nome': 'Meu amor'})
# adiciona_interesse(3,6)
# print(dic['PESSOAS'][0]['id'])
