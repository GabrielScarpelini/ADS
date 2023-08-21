def matriz(linhas,colunas):
    n = 1
    numeros = []
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(n)
            n += 1
            
        numeros.append(linha)
    return numeros 
                
                    
