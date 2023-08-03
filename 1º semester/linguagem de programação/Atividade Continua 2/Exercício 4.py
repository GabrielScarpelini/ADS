rest = int(input())
pag = int(input())
cont = 1
while rest > 0:
    print(f'pagamento: {cont}')
    print(f'antes = {rest}')
    rest -= pag
    cont += 1
    if rest < 0: 
        print(f'depois = 0')
        print('-----')
    else:
        print(f'depois = {rest}')
        print('-----')
    
