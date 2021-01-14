import unittest
import test_simple_calc as calc

class SimpleCalcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 6), 16)

    def test_sub(self):
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_sub_negative(self):
        self.assertEqual(calc.subtract(10, 15), -5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2, 5), 10)

    def test_multiply_negative(self):
        self.assertEqual(calc.multiply(6, -5), -30)

    def test_div(self):
        self.assertEqual(calc.divide(10, 5), 2)

    def test_div_negative(self):
        self.assertEqual(calc.divide(10, -2), -5)

if __name__ == '__main__':
    unittest.main()

