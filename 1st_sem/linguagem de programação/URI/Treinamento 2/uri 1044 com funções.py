# Funções
def entrada():
    (a, b)= input().split()
    a = int(a)
    b = int(b)
    return a, b 

def maior(n1, n2):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    return x, y 

def multiplos(n1, n2):
    resto = x % y
    multiplos = resto == 0
    if multiplos:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

# Código principal
v1 , v2 = entrada()
v3, v4 = maior(v1, v2)
multiplos(v3, v4)

