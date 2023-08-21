class Pessoa:
    def __init__(self):
        self.nome = input('Seu nome: ')
        self.salario = float(input('Salário '))
        self.contas = []

class Conta:
    def __init__(self):
        self.nome = input('qual conta que é: ')
        self.valor = float(input('qual o valor: '))

p1 = Pessoa()
enter = input('deseja adicionar conta (s/n): ')
total = 0
while enter != 'n':
    conta = Conta()
    p1.contas.append(conta)
    enter = input('deseja adicionar outra conta (s/n): ')

print(p1.contas[0].valor)

for i in p1.contas:
    total += p1.contas[i].valor

# print(f'olá {p1.nome}, o total se suas contas são {total} \
#       e o total que sobrerá será: {p1.salario - total}')