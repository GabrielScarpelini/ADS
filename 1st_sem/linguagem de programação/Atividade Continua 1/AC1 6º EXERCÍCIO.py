dia = input()
entrega = int(input())

if dia == 'domingo':
    dia = 1  

if dia == 'segunda':
    dia = 2 

if dia == 'terca':
    dia = 3 

if dia == 'quarta':
    dia = 4

if dia == 'quinta':
    dia = 5

if dia == 'sexta':
    dia = 6 

if dia == 'sabado':
    dia = 7

data = dia + entrega

if entrega == 0:
    print('chega hoje!')

elif data == 1 or data == 8:
    print('sera entregue domingo')
elif data == 2 or data == 9:
    print('sera entregue segunda')

elif data == 3 or data == 10:
    print('sera entregue terca')

elif data == 4 or data == 11:
    print('sera entregue quarta')

elif data == 5 or data == 12:
    print('sera entregue quinta')

elif data == 6 or data == 13:
    print('sera entregue sexta')

elif data == 7 or data == 14:
    print('sera entregue sabado')








    

      








