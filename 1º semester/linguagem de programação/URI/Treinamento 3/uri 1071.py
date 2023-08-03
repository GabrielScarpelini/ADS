def eh_impar(n):
    return n%2 != 0 

x = int(input())
y = int(input())

soma_impares = 0 


if y < 0:
    n = y + 2
else:
    n = y 

while n < x:
    if eh_impar(n):
        soma_impares += n
       
        
    n += 1

print(soma_impares)
