a, b = input().split()

a = int(a)
b = int(b)

resto = b % a
resto_= a % b 

if resto == 0 or resto_ == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos') 
