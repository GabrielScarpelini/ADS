coluna = int(input())
operator = input()
matriz = []
for _ in range(12):
    linha = []
    for _ in range(12):
        num = float(input())
        linha.append(num)

    matriz.append(linha)

soma = 0
for i in range(len(matriz)):
    soma += matriz[i][coluna]

if operator == 'S':
    print(f'{soma:.1f}')
elif operator == 'M':
    media = soma/12
    print(f'{media:.1f}')
