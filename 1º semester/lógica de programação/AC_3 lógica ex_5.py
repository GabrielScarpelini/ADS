def troca(v ,i ,j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
    return (v, i ,j)

def exibe(v, n):
    i = 0
    while i < n:
        print(v[i],end='')
        i += 1

    print()

    return(i,n)

def empurra(v,n):
    i = 0
    while i < n-1:
        while v[i] > v[i+1]:
            troca(v, i, i+1)

        i += 1

    return(v, n)

def bubble_sort(v, n):
    exibe(v ,n)
    tam = n
    while tam > 1:
        empurra(v, tam)
        exibe(v, tam)
        tam -= 1
    exibe(v, n)

    return(v, n)

bubble_sort([40,20,50,30,10],5)
