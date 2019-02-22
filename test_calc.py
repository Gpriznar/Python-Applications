
# confirm it that you need to have the test keyword
# name your file starting with the test keyboard
# test_thecomponentyouraretesting.py

# import unittest since we are using the testing
# features of Python language
import unittest
# importing Calculator class from calculator module
from new_calc import Calculator
# importing everything from myfunctions module
#from myfunctions import *

class CalculatorTests(unittest.TestCase):

    # setUp is called before running each test
    def setUp(self):
        # creating a property on the CalculatorTests class
        self.calculator = Calculator()
        print("SETUP")

    def test_add_two_numbers(self):
        print("test_add_two_numbers")
        #calculator = Calculator()
        result = self.calculator.add(2,3)
        self.assertEqual(5,result)

    def test_subtract_two_numbers(self):
        print("test_subtract_two_numbers")
        #calculator = Calculator()
        result = self.calculator.sub(5,2)
        self.assertEqual(3,result)

    def test_multiply_two_numbers(self):
        print("test_multiply_two_numbers")
        result = self.calculator.mult(10,5)
        self.assertEqual(50,result)

    def test_divide_two_numbers(self):
        print("test_divide_two_numbers")
        result = self.calculator.div(100,10)
        self.assertEqual(10,result)

    def tearDown(self):
        print("TEARDOWN")


# execute all tests in this class
unittest.main()
