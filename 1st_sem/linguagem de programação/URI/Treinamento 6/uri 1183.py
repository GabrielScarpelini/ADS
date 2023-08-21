operator = input()
matriz = []
for _ in range(12):
    linha  = []
    for _ in range(12):
        num = float(input())
        linha.append(num)
    matriz.append(linha)

soma = 0
lista_diag = []
for y in range(len(matriz)):
    for x in range(len(matriz)):
        if x > y:
            lista_diag.append(matriz[y][x])
            soma += matriz[y][x]

if operator == 'S':
    print(f'{soma:.1f}')
elif operator == 'M':
    media = soma/len(lista_diag)
    print(f'{media:.1f}')
