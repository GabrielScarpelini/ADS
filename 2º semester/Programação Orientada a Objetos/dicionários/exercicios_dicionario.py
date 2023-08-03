'''Exercício 01

Preencha um dicionário com as informações de 5 produtos.
Utilize o nome do produto como chave e o preço como valor. 
Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00

Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0, 'Lápis': 1.50}'''

dic = {}
for a in range(5):  
    produto = input()
    valor = float(input())
    dic[produto] = valor 

print(dic)

for chave in dic:
    if dic[chave] > 50:
        print(chave, dic[chave])

'''Exercício 02

Preencha um dicionário com os dados de 5 alunos.
Utilize o ra do aluno como chave e uma lista de três notas como valor.
Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.

Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}
'''
alunos = {}

while True:
    ra = input()
    if ra == '':
        break
    notas = []
    for n in range(3):
        n = float(input())
        notas.append(n)
    alunos[ra] = notas 

for u in alunos:
    media = sum(alunos[u])/len(alunos[u])
    print(media)

'''Exercício 3 
Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada e o valor é a quantidade de vezes que essa vogal aparece no texto. 
A função deve receber o texto como entrada, e retornar o dicionário.

Exemplo:
Para o texto abaixo:
'faculdade de tecnologia impacta'
A função deve retornar o seguinte dicionário:
{'a': 5, 'u': 1, 'e': 3, 'o': 2, 'i': 2}

# exemplo de como percorrer uma string
texto = 'faculdade de tecnologia impacta'
for c in texto:
  if c == 'a':	
'''

def conta_vogais(texto):
    dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for l in texto:
        if l == 'a':
            dic['a'] += 1  
        elif l == 'e':
            dic['e'] += 1
        elif l == 'i':
            dic['i'] += 1  
        elif l == 'o':
            dic['o'] += 1 
        elif l == 'u':
            dic['u'] += 1
    return dic
   
texto = input()

print(conta_vogais(texto))