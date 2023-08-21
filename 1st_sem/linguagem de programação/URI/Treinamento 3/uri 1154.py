n = int(input())
entradas = 1

x = n 
while n > 0:
    n = int(input())
    if n > 0:
        x += n 
        entradas += 1 

print(f'{x/entradas:.2f}')

    
