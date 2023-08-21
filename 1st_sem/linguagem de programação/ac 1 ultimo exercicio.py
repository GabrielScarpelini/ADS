dia = input()
tempo_entrega = int(input())
if dia == 'segunda':
    dia = 1
if dia == 'terça':
    dia = 2
if dia == 'quarta':
    dia = 3
if dia == 'quinta':
    dia = 4
if dia == 'sexta':
    dia = 5
if dia == 'sabado':
    dia = 6
if dia == 'domingo':
    dia = 7

data_entrega = (dia + tempo_entrega)%7

if tempo_entrega == 0: 
    print('sua entrega chega hoje')
if data_entrega == 1:
    print('sua entrega chega segunda')
if data_entrega == 2:
    print('sua entrega chega terça')
if data_entrega == 3:
    print('sua entrega chega quarta')
if data_entrega == 4:
    print('sua entrega chega quinta')
if data_entrega == 5:
    print('sua entrega chega sexta')
if data_entrega == 6:
    print('sua entrega chega sábado')
if data_entrega == 7:
    print('sua entrega chega domingo')
