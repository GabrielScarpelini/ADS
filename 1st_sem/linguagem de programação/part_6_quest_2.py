def contar(item,seq):
    i = 0
    cont = 0
    n = len(seq)
    while i < n:
        if item == seq[i]:
            cont += 1
        i += 1
    return cont
        
