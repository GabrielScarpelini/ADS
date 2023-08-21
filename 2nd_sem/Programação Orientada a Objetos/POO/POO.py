class ContaBancaria:
    
    def __init__(self, conta, nome):
        self.conta = conta
        self.nome = nome
        self.saldo = 0 
    
    def deposita_valor(self, valor):
        self.saldo += valor
    
    def sacar_valor(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

    def mostrar_valor(self):
        print(F'Saldo na conta é {self.saldo}')

conta = int(input("Nº da conta:"))
nome = input('Nome do Titular:')  

conta = ContaBancaria(conta, nome)
conta.mostrar_valor()
conta.deposita_valor(250)
conta.sacar_valor(500)