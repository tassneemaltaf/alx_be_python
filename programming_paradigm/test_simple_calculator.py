import unittest
from simple_calculator import SimpleCalculator

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(4, 2), 6)
        self.assertEqual(self.calc.add(-4, 3), -1)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(6, 3), 3)
        self.assertEqual(self.calc.subtract(8, 4), 4)
        self.assertEqual(self.calc.subtract(10, 9), 1)

    def test_mult(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(1, 3), 3)
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(6, 4), 24)
        self.assertEqual(self.calc.multiply(5, 5), 25)

    def test_div(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(12, 2), 6)
        self.assertEqual(self.calc.divide(20, 10), 2)
