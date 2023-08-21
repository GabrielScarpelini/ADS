
'''Exercício 01

Preencha uma lista com 10 números digitados pelo usuário e exiba:
o maior número da lista
o menor número da lista
a quantidade de números pares contidos na lista
a média dos números contidos na lista
todos os números menores do que a média calculada no item anterior'''

lista = [] 

for n in range(10):
    n = int(input())
    lista.append(n)

media = sum(lista) / len(lista)

print(max(lista))
print(min(lista))
print(len(lista))
print(media)

for n in lista:
    if n < media:
        print(n)


'''Exercício 02

Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista, gere uma lista com os números pares e outra com os números ímpares. 

Exemplo: 
Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8]. 
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]'''

lista = []
for n in range(10):
    n = int(input())
    lista.append(n)
par = []
impar = []
for n in lista:
    if n%2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(par)
print(impar)


'''Exercício 03

Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as duas tuplas e exiba a tupla resultante.
Dica: primeiro crie duas listas, e então, converta as listas em tuplas utilizando a função tuple.
tupla = tuple(lista)		# converte a lista em uma tupla

Exemplo: Suponha que as tuplas contenham os números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1).
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1).'''

lista1 = []
lista2 = []
for n in range(5):
    n = int(input())
    lista1.append(n)
for n in range(5):
    n = int(input())
    lista2.append(n)

tupla1 = tuple(lista1)
tupla2 = tuple(lista2)
print(tupla1 + tupla2)


'''Exercício 04

Escreva uma função chamada intercala_numeros que recebe como entrada duas listas de três elementos e retorna uma lista de seis elementos, com os números intercalados.

Exemplo: Suponha que as listas de entrada da função sejam: 
[1, 2, 3]
[4, 5, 6] 
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]'''

def intercala(lista, lista1):
    l_mais = []
    for n in range(len(lista)):
        l_mais.append(lista[n])
        l_mais.append(lista1[n])
    
    return l_mais

lista = []
lista1 = [] 
for n in range(3):
    n = int(input())
    lista.append(n)
for n in range(3):
    n = int(input())
    lista1.append(n)  

print(intercala(lista,lista1))



