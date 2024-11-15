import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(-3, 12), 9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-1, 2), -3)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 1), 6)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(65,5), 13)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(-18, 0), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(80,2), 0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(7,2), 1)
if __name__ == '__main__':
    unittest.main()