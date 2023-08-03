n = int(input())
nota = []
atv = []
lista = []
nota_alterada = 0 

for x in range(n):
    x = float(input())
    nota.append(x)
    lista.append(x)

for y in range(n):
    y = float(input())
    atv.append(y)

for i in range(n):
    nota_antes = nota[i]
    if atv[i] == 10:
        nota[i] += 2
        if nota[i] > 10:
            nota[i] = 10
    if nota_antes < nota[i]:
        nota_alterada += 1

print(f'NOTAS ALTERADAS: {nota_alterada}')
for i in range(5):
    if nota[i] == lista[i]:
        print(f'-({(i+1):03d}) original: {lista[i]:.2f} | final: {nota[i]:.2f}')
    else:
        print(f'*({(i+1):03d}) original: {lista[i]:.2f} | final: {nota[i]:.f2}')
