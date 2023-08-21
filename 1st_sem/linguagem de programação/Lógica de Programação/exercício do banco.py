salario = float(input('seu salário: '))


if salario >= 2000.00:
    tempo_contrato = int(input(f'anos de contrato: '))
    valor_emprestimo = float(input(f'valor do impréstimo: '))

    if tempo_contrato >= 2:
        valor_total = valor_emprestimo + valor_emprestimo*0.15
        print(f'valor total com juros é: {valor_total:.2f}')
    else:
        valor_total1 = valor_emprestimo +
        valor_emprestimo*0.20
        print(f'valor total com juros é: {valor_total1:.2f}')
else:
    print(f'seu empréstimo foi negado por não cumprir o requisito de salário',
          f' inferior a 2000.00')


        
        
    
