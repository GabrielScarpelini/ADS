cont = 0
lista = []
while cont < 10:
    n = int(input())
    lista.append(n)
    cont += 1 

for i in range(len(lista)):
    if lista[i] < 1:
        lista[i] = 1
    print(f'X[{i}] = {lista[i]}')
