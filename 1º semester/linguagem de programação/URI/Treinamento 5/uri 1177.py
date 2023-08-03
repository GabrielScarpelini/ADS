t = int(input())
lista = []
cont = 0

while cont < 1000:
    for i in range(t):
        lista.append(i)
    cont += 1 

for i in range(len(lista)):
    if i <= (cont-1):
        print(f'N[{i}] = {lista[i]}')
    else:
        break
