cont = 0
lista = []
n = int(input())
while cont < 10:
    lista.append(n)
    print(f'N[{cont}] = {lista[cont]}')
    n += n
    cont += 1
    

