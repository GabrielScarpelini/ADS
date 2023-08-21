l = int(input())

l26 = False

while not l26:
    if l >= 0 and l <=26:
        l26 = True
    else:
        l = int(input())

cont = 1

while cont <= l:
    num = 64 + cont 
    letra = chr(num)
    print(f'{letra*cont}')
    cont += 1 
