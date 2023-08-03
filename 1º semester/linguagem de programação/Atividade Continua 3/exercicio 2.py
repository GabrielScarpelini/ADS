n1 = int(input())
n2 = int(input())
if n1 > n2:
    print('Nenhuma tabuada no intervalo!')
else:
    while n1 <= n2:
        cont = 1
        while cont <= 10:
            result = n1 * cont
            print(f'{n1} x {cont} = {result}')
            cont += 1
        print('----------') 
        n1 += 1 
