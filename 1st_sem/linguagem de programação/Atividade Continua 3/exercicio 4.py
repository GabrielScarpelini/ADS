n = 1
lista = []
while n > 0:
    n = int(input())
    if n > 0:
        lista.append(n)
    
media = sum(lista)/len(lista)

print(f'MEDIA: {media:.2f}')
for elemento in lista:
    if elemento < media:
        print(elemento)
        
