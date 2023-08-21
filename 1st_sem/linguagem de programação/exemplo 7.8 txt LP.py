executa = input('Executar o bloco do laço: ')
contador = 0
while executa == 'sim':
    contador +=1
    executa = input('Executar o bloco do laço de novo: ')
print(f'O bloco do laço foi executado {contador} vezes')
