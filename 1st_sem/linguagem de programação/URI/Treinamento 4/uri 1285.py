def numero_repetido(string):
    for objeto in string:
        cont = string.count(objeto)
        if cont > 1:
            return True
        
    return False                        

while True:
    try:
        n1,n2 = input().split()
        inicio = int(n1)
        fim = int(n2)
        casa_dispo = 0
        while inicio <= fim:
            if numero_repetido(n1):
                inicio += 1
                n1 = str(inicio)
            else:
                inicio += 1
                casa_dispo += 1
                n1 = str(inicio)    


        print(casa_dispo)
    except EOFError:
        break
       

