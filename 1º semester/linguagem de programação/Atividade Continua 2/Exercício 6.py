def primo(n):
    if n == 1 or n == 0:
        return False
    else:
        cont = 2
        while cont < n:
            if n % cont == 0:
                return False
            else:
                cont += 1
        return True 
            



begin = int(input())
end = int(input())
cont_primo = 0 
while begin <= end:
    if primo(begin):
        print(begin)
        cont_primo += 1

    begin += 1 

print(f'primos: {cont_primo}')


