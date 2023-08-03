n = int(input())

cont = 1

fatorial = n 
 

while n < 0 or n > 13:
    n = int(input())

while cont != n:
    fatorial *= cont
    cont += 1
     
    
print(fatorial)
