from classes_to_test import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        two = Calculator.add(1, 1)
        self.assertEqual(two, 2)

    def test_subtract(self):
        three = Calculator.subtract(5, 2)
        self.assertEqual(three, 3)

    def test_multiply(self):
        eight = Calculator.multiply(4, 2)
        self.assertEqual(eight, 8)

    def test_divide_non_zero(self):
        four = Calculator.divide(12, 3)
        self.assertEqual(four, 4)

    def test_divide_by_zero(self):
        divide_by_zero = lambda: Calculator.divide(5, 0)
        self.assertRaises(ZeroDivisionError, divide_by_zero)

    def test_divide_by_zero_other(self):
        self.assertRaises(ZeroDivisionError, Calculator.divide, 5, 0)

    def test_divide_by_zero_context_manager(self):
        with self.assertRaises(ZeroDivisionError) as raise_context:
            Calculator.divide(5, 0)

        self.assertEqual(str(raise_context.exception), 'Num2 cannot be zero')


if __name__ == "__main__":
    unittest.main()
