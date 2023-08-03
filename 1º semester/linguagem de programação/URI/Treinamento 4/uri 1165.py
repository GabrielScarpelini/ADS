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
def casos():
    c = int(input())
    while c < 1 or c > 100:
        c = int(input())
    return c

def número():
    n = int(input())
    while n < 1 or n > 100000000:
        n = int(input())
    return n


rep = casos()
cont = 0
while cont < rep:
    n = número()
    if primo(n):
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')
    cont += 1 
