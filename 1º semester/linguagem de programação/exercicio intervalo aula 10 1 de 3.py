'''nota = float(input())

cont = 1

while nota < 0 or nota > 10:
    nota = float(input('Ops tente outro valor: '))
    cont += 1



print(f'{nota:.2f} e Número de vezes que foi testado é {cont}')'''


nota = float(input('Coloque um número: '))

cont = 1

limite = 3

limite_atingido = False

while (nota < 0 or nota > 10 and not limite_atingido:
    nota = float(input('Ops tente outro valor: '))
    cont += 1

    if cont == limite:
       limite_atingido = True

if limite_atingido:
       print('Você atingiu o limite máximo)
