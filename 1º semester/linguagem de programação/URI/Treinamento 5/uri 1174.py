cont = 0
lista = []
while cont < 100:
    n = float(input())
    lista.append(n)
    cont += 1
for i in range(len(lista)):
    if lista[i] <= 10:
        print(f'A[{i}] = {lista[i]}')
    

