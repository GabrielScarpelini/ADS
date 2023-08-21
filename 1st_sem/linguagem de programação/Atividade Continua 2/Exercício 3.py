vcs = float(input())
x = vcs

if vcs < 0:
    x = 0
    print(f'VC$ {x:.2f}')
    print(f'R$ {x * 2.50:.2f}')
else: 
    while vcs > 0:
        vcs = float(input())
        if vcs > 0:
            x += vcs
    

    print(f'VC$ {x:.2f}')
    print(f'R$ {x * 2.50:.2f}')
