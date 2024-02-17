import unittest

def soma(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(1, 5), 1)

if __name__ == '__main__':

	unittest.main()