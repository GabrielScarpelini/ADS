def entrada():
    n = 0
    cont = 1
    goahead = False
    while not goahead:
        n = input()
        cont += 1
        goahead = input('deseja continuar: s/n')
        if goahead == 's':
            goahead = True
    return n 
    
def inverte():
    entrada()
    


    
