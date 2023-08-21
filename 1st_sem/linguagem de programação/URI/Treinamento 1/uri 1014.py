nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas * 0.15
salario_com = salario + comissao
print(f'TOTAL = R$ {salario_com:.2f}') 
