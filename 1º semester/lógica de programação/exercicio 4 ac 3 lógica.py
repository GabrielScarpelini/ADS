def enigma(v,n):
    i = 0
    while i < n:
        v[i] = 2 * v[i]
        i += 2

    return (v)

def exibe(v,n):
    i = 0
    while i < n:
        print(f'{v[i]}')
        i += 1

    return (v)

v = [10,20,30,40,50]

enigma(v,len(v))

exibe(v,len(v))
