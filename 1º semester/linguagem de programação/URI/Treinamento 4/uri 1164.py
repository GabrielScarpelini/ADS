'''def perfeito(n):
    cont = 1
    soma = 0
    while cont <= n:
        if n % cont == 0:
            soma += cont
            cont += 1
        elif soma == n:
            return True
        elif soma > n:
            return False
        else:
            cont += 1
    return False'''

def perfeito(n):
    soma = 0
    for x in range(1,n):
        if n % x == 0:
            soma += x
    if soma == n:
        return True
    else:
        return False

def casos():
    n = int(input())
    while n < 1 or n > 20:
        n = int(input())
    return n

def numero():
    nro = int(input())
    while nro < 1 or nro > 10**8:
        nro = int(input())
    return nro

    

n = casos()
cont = 0

while cont < n:
    nro = numero()
    if perfeito(nro):
        print(f'{nro} eh perfeito')
    else:
        print(f'{nro} nao eh perfeito')

    cont += 1


    

    






        
