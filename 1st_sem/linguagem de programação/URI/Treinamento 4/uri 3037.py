teste = int(input())

cont_teste = 1

maria = 3
joao = 3 
totalm = 0
totalj = 0 
while cont_teste <= teste:
    while joao > 0:
        xj, dj = input().split()
        xj = int(xj)
        dj = int(dj)
        total_j = xj * dj
        totalj += total_j
        joao -= 1
    while maria > 0:
        xm, dm = input().split()
        xm = int(xm)
        dm = int(dm)
        total_m = xm * dm
        totalm += total_m
        maria -= 1
    if totalj > totalm:
        print('JOAO')
    else:
        print('MARIA')
    
    maria = 3
    joao = 3
    totalm = 0
    totalj = 0
    cont_teste += 1


 
