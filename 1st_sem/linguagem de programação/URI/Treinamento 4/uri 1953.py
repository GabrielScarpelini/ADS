def alunos():
    a = int(input())
    while a < 1 or a > 100000:
        a = int(input())
    return a
    
n = 0

while True:
    try:
        n = alunos()
        cont_epr = 0
        cont_ehd = 0
        intrusos = 0 
        cont = 0
        while cont < n:
            mat, cur = input().split()
            mat = int(mat)
            if cur == 'EPR':
                cont_epr += 1
            elif cur == 'EHD':
                cont_ehd += 1
            else:
                intrusos += 1
            cont += 1
        
  
        print(f'EPR: {cont_epr}')
        print(f'EHD: {cont_ehd}')
        print(f'INTRUSOS: {intrusos}')
    except EOFError:
        break







