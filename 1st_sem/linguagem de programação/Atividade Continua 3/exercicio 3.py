def cont_mil(x):
    div = x //1000
    if div >= 1:
        return div*1000
    else:
        return 0
    
qnt_canais = int(input())
cont = 0
lista= []
while cont < qnt_canais:
    canal = input().split(';')
    canal[1] = int(canal[1])
    canal[2] = float(canal[2])
    
    lista.append(canal)
    cont +=1 

premium = float(input())
ordinary = float(input())

print('-----\n'
      'BÔNUS\n'
      '-----')

for x in lista:
    comando = x[3]
    if comando == 'sim':
        bonus = (cont_mil(x[1]) / 1000)* premium + x[2]
    else:
        bonus = (cont_mil(x[1]) / 1000)* ordinary + x[2]
     
    print(f'{x[0]}: R$ {bonus:.2f}')
    
