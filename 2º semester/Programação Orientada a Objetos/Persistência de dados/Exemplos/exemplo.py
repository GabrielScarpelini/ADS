
# ler arquivo de texto linha por linha

arquivo = open("arquivo.txt", "r", encoding="UTF-8")    # r = read

for linha in arquivo:   # percorre o arquivo
    print(linha)        # imprime cada linha

arquivo.close()

#--------------------------------------------------------

# adicionar conteúdo em arquivo de texto já existente

# abre o arquivo para adicionar informações
arquivo = open('cadastro.txt', 'a', encoding='UTF-8')    # a = Append

# cadastra o nome e idade de 5 pessoas e adiciona no arquivo de texto
for i in range(5):
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    arquivo.write(nome + ' - ' + str(idade) + '\n')

arquivo.close()     # fecha o arquivo

#-------------------------------------------------------

# criar arquivo de texto

# O arquivo é criado no diretório do programa
# Se o arquivo já existe, será sobrescrito
arquivo = open("arquivo01.txt", "w", encoding="UTF-8")        # w =write

arquivo.write("Escreve uma linha\n")    # \n para pular as linhas
arquivo.write("Escreve outra linha\n")
arquivo.write(str(1.30) + "\n")         # converte numero para string

a = 100
arquivo.write(str(a) + "\n")            # escreve o conteudo de uma variável

arquivo.close()                         # fecha o arquivo

#------------------------------------------------------

# ler arquivo de texto

# o arquivo já deve existir
# procura no diretório do programa
arquivo = open("arquivo.txt", "r", encoding="UTF-8")      # r = read

# copia todo o conteúdo do arquivo para uma única variável string
a = arquivo.read()

print(a)    # imprime o conteúdo do arquivo no terminal

arquivo.close()                         # Fecha o arquivo