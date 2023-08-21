# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 8 alunos)
# Daniel Francelino de Oliveira		    RA	 2102588
# Diego Yann Lima Cardoso de Almeida    RA   2102876
# Felipe Singillo de Araujo			    RA   2103062
# Gabriel Scarpelini Pavia			    RA   2102341
# Gustavo Dias da Silva				    RA	 2102928
# Iago Henrique do Prado			    RA	 2102055
# Igor de Oliveira Pereira		        RA   2102141
# Jean Carlos Gomes de Oliveira		    RA   2102935


'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e dois itens e retorna True, se os dois itens estiverem
armazenado na lista, e False, caso contrário.
'''
def pertence(lista, item1, item2):
    if item1 and item2 in lista:
       return True
    else:
        return False



'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma lista e dois itens (velho e novo) e retorna uma lista onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''

def substituir(lista, velho, novo):
    lista2= []
    for i in range(len(lista)):
        if lista[i] == velho:
            lista2.append(novo) 
        else:
            lista2.append(lista[i])
    return lista2

'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    lista = []
    for i in range(len(tupla)):
        if tupla[i] == item:
            lista.append(i)
    return lista

'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
'''


def reprovados(alunos):
    rep = [] 
    for chave in alunos:
        media = sum(alunos[chave])/len(alunos[chave])
        if media < 6:
            rep.append(chave)
    return rep 


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações
'''


def excluir_nota(alunos, nome):
    if nome in alunos:
       alunos[nome].pop(0)
    return alunos
     


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada maior_nota que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a maior nota
de cada aluno.
'''


def maior_nota(alunos):
    dic = {}
    for nome in alunos:
        nota = max(alunos[nome])
        dic[nome] = nota
    return dic 