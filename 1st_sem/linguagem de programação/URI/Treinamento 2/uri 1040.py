(n1, n2, n3, n4)=input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

p1 = n1*0.2
p2 = n2*0.3
p3 = n3*0.4
p4 = n4*0.1 

media = p1 + p2 + p3 + p4


if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')

elif media < 5:
    media1 = media - 0.1
    print(f'Media: {media1:.1f}')
    print(f'Aluno reprovado.')

else:
    exame = float(input())
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {exame:.1f}')
    media_final = (exame + media)/2
    if media_final >=5.0:
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')
    
