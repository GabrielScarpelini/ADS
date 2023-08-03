from funcoes import converte_para_celsius, converte_para_fahrenheit

try:
    retorno = converte_para_fahrenheit(0)
    assert retorno == 32
    print('correta')
except AssertionError:
    print('Errada')

try:
    retorno = converte_para_fahrenheit(27)
    assert retorno == 80.6
    print('correta')
except AssertionError:
    print('Errada')

try:
    retorno = converte_para_celsius(32)
    assert retorno == 0
    print('correta')
except AssertionError:
    print('Errada')