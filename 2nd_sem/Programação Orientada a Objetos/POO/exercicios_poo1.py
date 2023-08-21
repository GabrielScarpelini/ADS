
'''Exercício 01 - Classe Livro
Implemente a classe Livro, conforme o diagrama a seguir. No programa
principal, crie dois objetos da classe Livro.

Atributos:
titulo
autor
quantidade_paginas

Métodos:
Essa classe não possui métodos'''
class Livro:

    def __init__(self, titulo, escritor, quantidade_paginas):
        self.titulo = titulo
        self.escritor = escritor
        self.quantidade_paginas = quantidade_paginas

    def exibe(self):
        print(f'{self.titulo}, {self.escritor}, {self.quantidade_paginas} ')

lista = []
while True:
    titulo = input('Nome do Livro:')
    if titulo =='':
        break
    autor = input('Autor:')
    n_pg = int(input('Quanta Páginas Possui:'))

    livro1 = Livro(titulo, autor, n_pg)
    lista.append(livro1)
    
for livro in lista:
    livro.exibe()



'''Exercício 02 - Classe Triangulo
Crie uma classe que representa um triângulo.

Atributos:
lado_a
lado_b
lado_c

Métodos:
calcular_perimetro: retorna o perímetro do triângulo (soma dos três lados).

Crie um programa que utilize esta classe. O programa deve pedir ao usuário
        que informe as medidas dos três lados de um triângulo. 
Depois deve criar um objeto com essas medidas e exibir seu perímetro.'''
   

class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c 
    
    def perimetro(self):
        return (self.lado_a + self.lado_b + self.lado_c)
    

lado1 = int(input('Tamanho do lado:'))
lado2 = int(input('Tamanho do 2ª lado:'))
lado3 = int(input('por fim o tamanho da reta:'))

tri = Triangulo(lado1, lado2, lado3)
print(tri.perimetro())



'''Exercício 03 - Classe Televisão
Implemente a classe Televisao.

Atributos:
canal (o canal inicial da tv deve ser None)
volume (o volume inicial da tv deve ser zero)

Métodos:
aumentar_volume: aumenta o nível de volume em uma unidade.
diminuir_volume: diminui o nível de volume em uma unidade.
alterar_canal: recebe o número do canal que será sintonizado e altera o 
canal da tv.

Faça um programa para criar um objeto da classe Televisao e testar a sua classe. 
Veja abaixo um trecho de programa que utiliza a classe:'''

class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1 
        
    def diminuir_volume(self):
        self.volume -=1

    def alterar_canal(self, valor):
        self.canal = valor

   
tv = Televisao()  
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')             # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')           # o volume da tv é 2 

"""Exercício 04 - Classe Funcionário
Implemente uma classe Funcionario. 

Atributos:
nome
salario

Métodos:
aumentar_salario: recebe como parâmetro de entrada um percentual
 e altera o salário do funcionário, de acordo com o percentual recebido.

Crie um programa que utilize esta classe. O programa deve pedir ao usuário
o nome e o salário do funcionário e criar um objeto da classe Funcionario. 
Depois, deve solicitar ao usuário o percentual de aumento e executar o 
método aumentar_salario. Na sequência deve imprimir
o salário do funcionário atualizado
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentar_salario(self, percentual):
        self.salario += self.salario * percentual/100
        

nome = input('Informe seu nome: ')
salario = float(input('Informe seu salário: '))

employee = Funcionario(nome, salario)

percent = float(input('Informe o percentual de aumento salarial: '))

employee.aumentar_salario(percent)

print(f'salario: {employee.salario:.2f}')  # tem que expecificar o .atributo