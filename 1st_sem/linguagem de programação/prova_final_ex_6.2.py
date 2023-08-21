def pede_numeros():
    entrada = False
    lista = []
    while not entrada:
        num = input()
        if num == "":
            entrada = True
        else:
            num = float(num)
            lista.append(num)
    return lista

def calcula_media(seq):
    soma = 0
    for n in seq:
        soma += n
    final = soma / len(seq)
    return final

def calcula_mediana(seq):
    seq.sort()
    if len(seq) % 2 == 0:
        i = (len(seq)/2) - 1
        i = int(i)
        med1 = seq[i]
        med2 = seq[i+1]
        mediana = (med1+med2)/2
        return mediana
    else:
        i = len(seq)//2
        return seq[i]

def desvio_padrao(seq):
    soma = 0
    for i in range(len(seq)):
        calculo = ((seq[i] - calcula_media(seq))**2)
        soma += calculo
    devp = (soma / (len(seq)-1))**0.5
    return devp

