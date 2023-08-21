class Produto:
    def __init__(self, nome, preco): # atribuindo nome e preço aos produtos
        self.nome = nome 
        self.preco = preco 

class Cliente:
    def __init__(self, nome):  #Atribuindo o nome do cliente 
        self.nome = nome

class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente 
        self.produtos = []

    def adicionar_produto(self, produto): #Adciona os produtos no self.produtos
        self.produtos.append(produto)

    def listar_produtos(self):  
        print('Nome do cliente: ', self.cliente.nome) # caminho para nome do cliente 
        for prod in self.produtos:
            print(prod.nome, prod.preco)    
    
    def calcular_total(self):
        soma = 0 
        for prod in self.produtos:
            soma += prod.preco
        print(f'Total da compra: {soma:}')


cliente1 = Cliente('Gabriel', )

produto1 = Produto('Pen drive', 30)
produto2 = Produto('HD',500)
produto3 = Produto('Celular', 1400)

carrinho1 = Carrinho(cliente1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto1)
carrinho1.adicionar_produto(produto3)


carrinho1.listar_produtos()
carrinho1.calcular_total()