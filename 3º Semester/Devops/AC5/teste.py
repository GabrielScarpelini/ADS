import abc
from unittest import TestCase, main
from calculadora import Calculadora

class Teste(TestCase):

    def test_divisao(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(21, 3), 7)

    def test_divisao_dois(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(81, 9), 9)
    
    def test_divisao_tres(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(81, 9), 9)
    
    def test_divisao_zero(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(0,7), 0)

    def test_divisao_zero_dois(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(7,0), 0)

    def test_mult(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(5,5), 25)
    
    def test_mult2(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(5,10), 50)
    
    def test_mult3(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(9,9), 81)
    
    def test_mult_zero(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(9,0), 0)
    
    def test_mult_zero_dois(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(0,9), 0)

    def test_soma(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(89,81), 170)
    
    def test_soma_dois(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(100,-99), 1)

    def test_soma_tres(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(1000,599), 1599)

    def test_soma_quad(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(999,699), 1698)

    def test_soma_quint(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(333,666), 999)

    def test_menos_um(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrair(1000,998), 2)

    def test_menos_dois(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrair(1500,25), 1475)

    def test_menos_tres(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrair(1500,75), 1425)

    def test_menos_quad(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrair(1998,2000), -2)
    
    def test_menos_quint(self):
        calc = Calculadora()
        self.assertEqual(calc.subtrair(666,1998), -1332)


if __name__ =='__main__':
    main()