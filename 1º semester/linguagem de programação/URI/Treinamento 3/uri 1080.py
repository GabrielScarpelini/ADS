cont = 1
x = -1
y = cont 
while cont <= 100:
    n = int(input())
    if n > x:
        x = n
        y = cont
    cont += 1 
        
print(f'{x}\n'
      f'{y}')

        

