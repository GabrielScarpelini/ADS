#print(len('Utilize o método aumentar_salario para atualizar os salários dos funcionários'))
class ContaBancaria:
    
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = 0
        
    
    def depositar(self, valor, senha):
        if senha == self.senha:
            self.saldo += valor
        else:
            print('Senha Incorreta')
            

    def sacar(self, valor, senha):
        if senha == self.senha:
            if self.saldo >= valor:
                self.saldo -= valor
                return True
            else:
                print('Saldo insuficiente')
        else:
            print('Senha incorreta')
            return False    
            
pessoa1 = ContaBancaria(1234, 'Gabriel', 123456)
print('Saldo: ', pessoa1.saldo)

tentativas = 0
while tentativas < 4:
    senha = int(input('Sua Senha: '))
    if senha =='':
        break
    pessoa1.depositar(500, senha)
    if pessoa1.sacar(450, senha) == False:
        tentativas += 3 


print(pessoa1.saldo)

