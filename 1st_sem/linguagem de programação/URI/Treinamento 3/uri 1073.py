def eh_par(n):
    return n % 2 ==0

soma_pares = 1 

n = int(input())

while n <=5 or n >= 2000:
    n = int(input())
    

while soma_pares <= n:
    if eh_par(soma_pares):
        print(f'{soma_pares}^2 = {soma_pares**2}')
    soma_pares += 1
