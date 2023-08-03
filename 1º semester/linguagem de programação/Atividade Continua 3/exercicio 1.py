def pertence(v, lista):
    for elemento in lista:
        if v == elemento:
            return True
    return False
            
entrada = input().split()
lista = []
for elemento in entrada:
    elemento = int(elemento)
    lista.append(elemento)
while entrada!= 'encerrar':
    entrada = input().split()
    comando = entrada[0]
    if comando == 'exibir':
        lista.sort()
        print(*lista)
    elif comando == 'adicionar':
        n = entrada[1]
        n = int(n)
        lista.append(n)
    elif comando == 'remover':
        n = entrada[1]
        n = int(n)
        if pertence(n,lista):
            lista.remove(n)
        else:
            print(f'código {n} não encontrado')
    else:
        entrada = 'encerrar'

lista.sort()
print(*lista)
