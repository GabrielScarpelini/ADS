def eh_par(x):
    resto = x % 2
    if resto == 0:
        return True
    else:
        return False

def entrada ():
    n = int(input())
    return n

n1 = entrada ()
n2 = entrada ()
n3 = entrada ()
n4 = entrada ()
n5 = entrada ()

numeros_pares = 0

if eh_par(n1):
    numeros_pares += 1
if eh_par(n2):
    numeros_pares += 1
if eh_par(n3):
    numeros_pares += 1
if eh_par(n4):
    numeros_pares += 1
if eh_par(n5):
    numeros_pares += 1

print(f'número de pares é: {numeros_pares}')   
    
