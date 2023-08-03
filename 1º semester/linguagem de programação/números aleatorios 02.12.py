from random import randint

def aleatorio():
    n = int(input())
    top = n**2
    botton = -n**2
    lista = []
    for x in range(n):
        valor = randint(botton, top)
        lista.append(valor)
    return lista 
