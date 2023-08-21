'''Exercício 01
Nesta questão você deve identificar as partes problemáticas do código e reescrevê-lo utilizando tratamento de exceções. 
Ou seja, devem ser identificadas todas as exceções que podem ser geradas e, para cada uma, deve ser dado o tratamento adequado que, nesse exercício, 
significa alertar o usuário quanto ao problema. 
'''

try:
    x = int(input('Primeiro valor:'))
    y = int(input('Segundo valor:'))
    z = x / y
    print('O resultado da divisão é:', z)

except ZeroDivisionError:
    print('Não é possível dividir por Zero')
except ValueError:
    print('Ops isso não é um número')
except Exception:
    print('Ops algo deu errado')
finally:
    print('Código continua funcionando')

'''Exercício 02
O código abaixo lança uma exceção e interrompe a execução do programa. 
Utilizando tratamento de exceções, corrija o programa com o objetivo de alertar o 
usuário sobre o erro ocorrido, e impedir que o programa seja interrompido bruscamente.'''

def funcao_1():
    print('Início da função')
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        print(lista[i])
    print('Fim da função')
 
try:
    print('Início do programa')
    funcao_1()
    print('Fim do programa')
except IndexError:
    print('A lista acessada não possui o índice informado')

'''Exercício 03
Preencha uma lista com 5 nomes de pessoas, informados pelo usuário.
Criar uma função que recebe como parâmetro de entrada a lista e uma posição (índice)
 dessa lista e retorna o nome que está nessa posição. 
Essa função deve gerar e tratar uma exceção do tipo IndexError caso o índice não 
exista na lista'''



def posicao(lista,index):
    try:
        return print(lista[index])
    except IndexError:
        return print('Esse índice não está presente nesta lista')

lista = []
while True:
    nome = input('Nome: ')
    if nome == '':
        break
    lista.append(nome)

print(lista)
indice = int(input('Informe o Indice: '))
print(posicao(lista,indice))

'''Exercício 04
Crie um dicionário para armazenar uma listagem de alunos. 
Utilize como chave o RA do aluno e como valor o nome do aluno.
Os dados devem ser informados pelo usuário
O RA de cada aluno deve ser composto por um número inteiro de exatamente 7 dígitos.
Caso o RA informado não esteja no formato correto, deve ser gerada uma exceção do tipo ValueError (utilize a instrução raise).
Caso o RA informado já exista no dicionário, deve ser gerada uma exceção do tipo TypeError (utilize a instrução raise).

Observação: Você pode utilizar o código abaixo como exemplo e alterá-lo para gerar e tratar as exceções solicitadas.
'''

alunos = {}
try:
    while True:    
        ra = input('RA: ')
        if ra =='':
            break 
        if len(ra) < 7:
            raise ValueError ('Ra informado tem menos de 7 caracteres')
        if len(ra) > 7:
            raise ValueError ('RA informado é tem mais de 7 caracteres')      
        if ra in alunos:
            raise TypeError
        nome = input('Nome: ')
        alunos[ra] = nome
              
        
except ValueError as mensagem:
    print('Erro:', mensagem)
except TypeError:
    print('ERRO: Esse RA já foi inserido')

print(alunos)

'''Importe o módulo abaixo para um programa de teste e escreva testes 
unitários para as funções do módulo:''' 

def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius

def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

try:
    a = converte_para_celsius(32)
    assert a == 0
    print('Correto')
    b = converte_para_celsius(41)
    assert b == 5.0
    print('Correto')
    c = converte_para_fahrenheit(0)
    assert c == 32.0
    print('Correto')
    d = converte_para_fahrenheit(27)
    assert d == 80.6
    print('Correto')
except AssertionError:
    print('Erro')
