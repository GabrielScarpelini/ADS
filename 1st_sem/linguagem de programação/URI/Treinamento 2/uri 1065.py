a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

total_pares = 0

if a % 2 == 0:
    total_pares += 1
if b % 2 == 0:
    total_pares += 1 
if c % 2 == 0:
    total_pares += 1
if d % 2 == 0:
    total_pares += 1
if e % 2 == 0:
    total_pares += 1 

print(f'{total_pares} valores pares')

'''
podia ter sido assim tbm

a = int(input())
if a % 2 == 0:
    total_pares += 1
'''



    
    
