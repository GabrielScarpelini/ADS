def calcula_volume(comprimento, largura, altura):

    return comprimento * largura * altura



def converte_para_celsius(fahrenheit):

    celsius = (5.0/9.0) * (fahrenheit - 32)

    return celsius


def converte_para_fahrenheit(celsius):

    fahrenheit = 1.8 * celsius + 32

    return fahrenheit

try:
    resultado = calcula_volume(1, 1, 1)
    assert resultado == 1
    print("caso1 : volume correto 1 ")
except:
    AssertionError
    print("caso1 :é diferente de 1")

try:
    resultado = calcula_volume(2, 4, 3)
    assert resultado == 24
    print("caso2 :volume correto 24")
except:
    AssertionError
    print(f"é diferente de 24")

try:
    resultado = calcula_volume(5, 5, 2)
    assert resultado == 50
    print("caso3 :volume correto 50")
except:
    AssertionError
    print("caso3 :é diferente de 50")


try:
    resultado = converte_para_fahrenheit(0)
    assert resultado == 32
    print("caso1 :fahrenheit correto 32")
except:
    AssertionError
    print("caso1 :é diferente de 32")

try:
    resultado = converte_para_fahrenheit(27)
    assert resultado == 80.6
    print("caso2 :fahrenheit correto 80.6")
except:
    AssertionError
    print("caso2 :é diferente de 80.6")

try:
    resultado = converte_para_celsius(32)
    assert resultado == 0
    print("caso3 :celsius correto 0")
except:
    AssertionError
    print("caso3 :é diferente de 0")

