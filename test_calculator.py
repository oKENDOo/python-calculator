import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(5, 5), 10)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(11, 9), 20)

    def test_sub1(self):
        self.assertEqual(self.calc.subtract(52, 12), 40)

    def test_sub2(self):
        self.assertEqual(self.calc.subtract(10, 10), 0)

    def test_multi1(self):
        self.assertEqual(self.calc.multiply(8, 5), 40)
    
    def test_multi2(self):
        self.assertEqual(self.calc.multiply(800, 0), 0)

    def test_div1(self):
        self.assertEqual(self.calc.divide(50, 5), 10)
    
    def test_div2(self):
        self.assertEqual(self.calc.divide(800, 1),800 )

    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10,5), 0)
    
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(55, 10), 5)



if __name__ == '__main__':
    unittest.main()