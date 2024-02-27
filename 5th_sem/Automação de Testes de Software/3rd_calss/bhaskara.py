import math


class ExcecaoNaoEhEquacaoSegundoGrau(Exception):
    pass


def calcular_delta(a, b, c):
    return b * b - 4 * a * c


def calcular_raizes(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta == 0:
        raiz = -b / (2 * a)
        return 1, raiz
    else:
        if delta < 0:
            return 0
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            return 2, raiz1, raiz2 
        
# caixa branca 
# caixa branca 
# caixa branca 
# caixa branca 
# caixa branca 
# caixa branca 
# caixa branca 
# caixa branca 
# caixa branca 