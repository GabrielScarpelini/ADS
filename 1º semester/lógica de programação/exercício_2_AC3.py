x = int(input())
y = int(input())
contbd = 0
contbt = 0
contbn = 0 
i = 0
while i < x:
    contbd += 1
    j = 0
    while j < y:
        contbt += 1
        j += 1
    i += 1
contbn += 1

print(contbd)
print(contbt)
print(contbn)
        
