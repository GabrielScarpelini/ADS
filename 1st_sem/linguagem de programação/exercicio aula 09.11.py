'''numero = int(input())
n = int(input())
cont = 0

while cont < n:
    numero += 1
    print(numero)
    cont += 1'''

'''n = 10
while 0 <= n:
    print(n)
    n -= 1
print('Fogo')'''

def eh_par(n):
    return x % 2 == 0


num1 = int(input())
num2 = int(input())

total_pares = 0 
total_impares = 0 
soma_pares = 0
soma_impares = 0 

x = num1

while x <= num2:
    if eh_par(x):
        total_pares += 1
        print(x)
        soma_pares += x
    else:
        total_impares +=1
        soma_impares += x 
    x += 1 

'''print(f'Total de Pares é:{total_pares} entre [{num1},{num2}]')
print(f'{total_impares} impares foram ignorados')
print()
print(f'Soma dos pares {soma_pares}')
print(f'Soma dos impares {soma_impares}')'''

