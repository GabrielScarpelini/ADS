credito = float(input('quanto de crédito possui: '))
total_compra = 0
contador = 1 
itens_comprados = 0 



while credito > 0:
    valor_produto = float(input(f'valor do produto {contador}: '))    
    if valor_produto < credito:
        contador += 1
        itens_comprados += 1 
        total_compra += valor_produto
        credito -= valor_produto
    
       
       
print(f'A compra {contador} foi cancelada!')
print(f'itens comprados = {itens_comprados}')
print(f'Valor total = {total_compra:.2f}')
print(f'Crétido restante = {credito:.2f}')

    
    
