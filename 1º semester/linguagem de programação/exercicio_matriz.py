#lição de criar matrizes 
from pprint import pprint
def resultado(line,colun):
    n = 1 
    matriz = []
    for x in range(line):
        line = []
        for j in range(colun):
            line.append(f'{n:2}')
            n += 1
        matriz.append(line)
        
    
    return matriz
        
matriz = resultado(5,6)  
pprint(matriz, width = 50)


#RESPODIDO PELO PROF
'''para cópias usamos'''

list(lista)

var = lista[:]
var = lista.copy()
copy.copy(lista) #acho que tem que importar algo

