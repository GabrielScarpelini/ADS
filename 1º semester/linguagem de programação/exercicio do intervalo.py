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

x = num1

while x <= num2:
    if eh_par(x):
        total_pares += 1
        print(x)

    x += 1 

print(f'Total de Pares é:{total_pares} entre [{num1},{num2}]')

