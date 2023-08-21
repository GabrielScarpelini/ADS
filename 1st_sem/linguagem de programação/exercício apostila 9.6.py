qnt_salario = int(input())
i = 0 
soma = 0
salario = []
for _ in range(qnt_salario):
    salary = float(input('Salário: R$'))
    salario.append(salary)
    soma += salary
    
    
media = soma / qnt_salario



for salary in salario:
    if salary < media:
        print(f'Salário {salary:.2f} está abaixo da média')
    else:
        print(f'Salário {salary:.2f} está acima de média')

    
