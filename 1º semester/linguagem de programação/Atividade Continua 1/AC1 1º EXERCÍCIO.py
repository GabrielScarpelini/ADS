'''
valor = float(input())

quantidade = int(input())

valor_total = valor * quantidade 

quantidade_de_disconto = 0

if quantidade != 0:
    quantidade_de_disconto += quantidade

valor_do_disconto = quantidade_de_disconto/100

disconto = valor_total * (0.1 + valor_do_disconto)

valor_real= valor_total - disconto 


print(f'{valor_total:.2f}\n{valor_real:.2f}')
'''
valor = float(input())

quantidade = int(input())

valor_total = valor * quantidade

quantidade_de_disconto = quantidade/100

disconto = valor_total * (0.1+quantidade_de_disconto)

valor_real = valor_total - disconto

print(f'{valor_total:.2f}\n{valor_real:.2f}')

