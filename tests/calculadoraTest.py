import unittest
from calculadora import soma, subtracao, multiplicacao, divisao, calculadora, run_calculadora
from io import StringIO
import sys

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 2), 3)
        self.assertEqual(subtracao(-1, -1), 0)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(2, 3), 6)
        self.assertEqual(multiplicacao(-1, 1), -1)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertEqual(divisao(10, 2), 5)
        self.assertEqual(divisao(0, 5), 0)

    def test_divisao_por_zero(self):
        self.assertEqual(divisao(6, 0), "Não é possivel dividir por zero")
        self.assertEqual(divisao(10, 0), "Não é possivel dividir por zero")

    def test_soma_com_negativos(self):
        self.assertEqual(soma(-8, 3), -5)

    def test_subtracao_com_decimais(self):
        self.assertEqual(subtracao(7.5, 2.5), 5.0)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(multiplicacao(6, 0), 0.0)

    def test_entrada_invalida_para_escolha(self):
        self.assertEqual(calculadora(5), "Escolha inválida!")

    def test_entrada_invalida_para_numeros(self):
        sys.stdin = StringIO('1\nabc\ndef\n')
        self.assertEqual(calculadora('1'), "Entrada inválida!")

    # Restaurando o fluxo de entrada padrão
    def tearDown(self):
        sys.stdin = sys.__stdin__

if __name__ == '__main__':
    unittest.main()