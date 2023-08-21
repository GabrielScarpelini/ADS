a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a
    
resto = maior % menor
multiplos = resto == 0 

if multiplos:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
