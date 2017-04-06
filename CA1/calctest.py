import calccode #import python file with calccode
import unittest #import test module from python libary to run tests on calccode

class TestCalculator(unittest.TestCase): #setting up class for test,can access in other files. 

    def setUp(self):
        self.calc = calccode.mathcalc() #pointing to the calculator code in other file 
		
    def test_calc_add(self): #testing for addition 
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
        result = self.calc.add(2,4)
        self.assertEqual(6, result)
        result = self.calc.add(2, -2)
        self.assertEqual(0, result)

	
    def test_calc_subtract(self):
        result = self.calc.subtract(2, 2)
        self.assertEqual(0, result)
        result = self.calc.subtract(2,4)
        self.assertEqual(-2, result)
        result = self.calc.subtract(2, -4)
        self.assertEqual(6, result)
		


    def test_calc_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        self.assertRaises(ValueError, self.calc.subtract, 'two', 'three')
	print ('so far so good')
		
    def test_calculator_multiply_returns_correct_result(self):
        result = self.calc.multiply(2, 2)
        self.assertEqual(4, result)
        result = self.calc.multiply(2,4)
        self.assertEqual(8, result)
        result = self.calc.multiply(2, -2)
        self.assertEqual(-4, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)

	print ('so far so good')


    def test_calc_divide_method_returns_correct_result(self):
		result = self.calc.divide(2, 2)
		self.assertEqual(1, result)
		result = self.calc.divide(4,2)
		self.assertEqual(2, result)
		result = self.calc.divide(2, -2)
		self.assertEqual(-1, result)
		result = self.calc.divide(2, 4)
		result = self.calc.divide(2, 0)
		self.assertEqual ('error', result) #checking zero division error 
		self.assertRaises(ValueError, self.calc.divide, 'two', 'three')
		self.assertRaises(ValueError, self.calc.divide, 'two', 0)
		self.assertRaises(ValueError, self.calc.divide, 2, 'three')
	

    def test_calc_exp_method_returns_correct_result(self):
        result = self.calc.exp(2, 2)
        self.assertEqual(4, result)
        result = self.calc.exp(2,4)
        self.assertEqual(16, result)
        result = self.calc.exp(2, -2)
        self.assertEqual(0.25, result)
        result = self.calc.exp(2, 0)
        self.assertEqual(1, result)

		
    def test_calc_sq_method_returns_correct_result(self):
        result = self.calc.sq(2,)#only one number required for test 
        self.assertEqual(4, result)
        result = self.calc.sq(5,)
        self.assertEqual(25, result)
        result = self.calc.sq(16,)
        self.assertEqual(256, result)
        result = self.calc.sq(1,)
        self.assertEqual(1, result)	
	

    def test_calc_sqroot_method_returns_correct_result(self):
        result = self.calc.sqroot(100,)
        self.assertEqual(10, result)
        result = self.calc.sqroot(25,)
        self.assertEqual(5, result)
        result = self.calc.sqroot(256,)
        self.assertEqual(16, result)
        result = self.calc.sqroot(1,)
        self.assertEqual(1, result)	
	

    def test_calc_sin_method_returns_correct_result(self):
        result = self.calc.sin(100,)
        self.assertEqual(-0.5063656411097588, result) #tried to shorten numbers here, only 3 places after decimal but python didnt like this, could have perhaps added more code to overcome this
        result = self.calc.sin(12,)
        self.assertEqual(-0.5365729180004349, result)
        result = self.calc.sin(256,)
        self.assertEqual(-0.9992080341070627, result)
        result = self.calc.sin(1,)
        self.assertEqual( 0.8414709848078965, result)	
	
	
    def test_calc_cos_method_returns_correct_result(self):
        result = self.calc.cos(100,)
        self.assertEqual( 0.8623188722876839, result)
        result = self.calc.cos(12,)
        self.assertEqual(0.8438539587324921, result)
        result = self.calc.cos(256,)
        self.assertEqual(-0.03979075993115771, result)
        result = self.calc.cos(1,)
        self.assertEqual( 0.5403023058681397, result)	
	

    def test_calc_tan_method_returns_correct_result(self):
        result = self.calc.tan(100,)
        self.assertEqual( -0.5872139151569291, result)
        result = self.calc.tan(12,)
        self.assertEqual(-0.6358599286615808, result)
        result = self.calc.tan(256,)
        self.assertEqual(25.111559463448298, result)
        result = self.calc.tan(1,)
        self.assertEqual( 1.5574077246549023, result)	
	print ('glad to be finished the test code')	
	
if __name__ == '__main__':
    unittest.main()

#could have tested more "tricker numbers"....math _espeically sin,cosine,tan_not my strongest tests above.
#C:\Users\carrm\Desktop\CA1>calctest.py
# ....so far so good
# .....glad to be finished the test code
# .so far so good
# .
# ----------------------------------------------------------------------
# Ran 11 tests in 0.000s

# OK

# C:\Users\carrm\Desktop\CA1>