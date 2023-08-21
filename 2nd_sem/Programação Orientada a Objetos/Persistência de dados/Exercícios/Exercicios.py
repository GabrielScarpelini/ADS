'''Exercício 01

Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada linha).
'''
arquivo = open("lista10.txt", 'a', encoding='UTF-8')

for i in range(10):
    num = input('Digite um Número:')
    arquivo.write(str(num) + '\n')

'''Exercício 02

Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório de todos os números contidos no arquivo
'''

arquivo = open("lista10.txt", "r", encoding="UTF-8")
soma = 0
for linha in arquivo:
    print(linha)
    soma += int(linha)
print(soma)

"""Exercício 03

Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário grave diversos caracteres
 nesse arquivo até que o mesmo entre com o caractere “0” (zero). 
"""

arquivo = open('arquivo.txt', 'a', encoding='UTF-8')

while True: 
    a = input('Digite qualquer coisa: ')
    a = str(a)
    if a == '0':
        break
    elif a == int:
        arquivo.write(a + "\n")
    else:
        arquivo.write(a + '\n')

'''Exercício 04

Faça um programa que abra um arquivo de texto e mostre no terminal quantos caracteres desse arquivo são vogais
'''

arquivo = open('lista10.txt', 'r', encoding="UTF-8")
vogais = ['a','e','i','o','u','A','E','I','O','U']
soma = 0
for linha in arquivo:
    for x in linha:
        if x in vogais:
            soma += 1
print(soma)



"""Exercício 05

Faça um programa que solicite o ano atual ao usuário. Abra um arquivo chamado “arq.txt” que contém um conjunto 
de dados formados por nomes e datas de nascimento, conforme o exemplo abaixo. 
Ingrid 16 05 2000
Lucas 08 10 1997
Fernanda 28 06 2000
João 06 12 1994
Isabella 27 11 1997



O programa deve imprimir na terminal o nome e a idade que essa pessoa terá ou têm nesse ano, no formato:
Ingrid 22
Lucas 25
Fernanda 22
João 28
Isabella 25

"""

arquivo = open('arq.txt', 'r', encoding="UTF-8")
show = 0
for x in arquivo:
    ano = x[-5:] 
    ano = int(ano)
    show = 2022 - ano
    show = str(show)
    nome = x.find(' ')
    print(x[:nome], show )

"""Exercício 06
Utilize o bloco de notas para criar dois arquivos de texto. Um arquivo apenas com números pares, e outro apenas 
com números ímpares.

Coloque um número em cada linha do arquivo. Os números podem estar em qualquer ordem.

Faça um programa que abra os dois arquivos e gere um terceiro arquivo com todos os números, em ordem crescente.
Deve ser colocado um número em cada linha.

Exemplo:
Arquivos de Entrada:

4
22
2
100
38


99
1
13
53
71
19


Arquivo de Saída:
1
2
4
13
19
22
38
53
71
99
100



"""

arquivo1 = open('lista1.txt', 'r', encoding="UTF-8")
arquivo2 = open('lista2.txt', 'r', encoding="UTF-8")
arquivo3 = open('lista.txt','a', encoding="UTF-8")

lista = []

for linha in arquivo1:
    lista.append(int(linha))

for linha in arquivo2:
    lista.append(int(linha))
lista.sort()

for i in lista:
    arquivo3.write(str(i) +'\n')

