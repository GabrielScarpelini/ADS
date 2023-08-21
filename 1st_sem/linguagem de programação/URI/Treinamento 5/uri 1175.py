cont = 0
lista = []
while cont < 20:
    n = int(input())
    lista.append(n)
    cont += 1
lista.reverse()
for i in range(len(lista)):
    print(f'N[{i}] = {lista[i]}')    
