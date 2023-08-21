def eh_impar(n):
    return n % 2 != 0 

n = int(input())

cont = 1

while cont <= n:
    if eh_impar(cont):
        print(cont)

    cont += 1 
    
   
    
