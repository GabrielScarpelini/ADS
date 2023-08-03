operator = input()
matriz=[]
for _ in range(12):
    linha = []
    for _ in range(12):
        num = float(input())
        linha.append(num)
    matriz.append(linha)

linha = 1
coluna = 1
canto = []
for y in range(len(matriz)):
    for x in range(len(matriz)):
        if y == -x:
            canto.append(matriz[y][x])
            canto.append(matriz[y][x-coluna])
            
                                    

print(len(canto))
