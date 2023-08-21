soma = 0
cont = 1
i = 0
salario = []
while salario[i] >= 0:
    salario[i] = int(input())
    if salario[i] >= 0:
        cont += 1
        soma += salario[i]
    else:
        cont -= 1

media = soma / cont


