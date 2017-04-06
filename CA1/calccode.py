import math
#import python module to run calculations

			
class mathcalc(object): #setting up class for calculator. can reference this class in seperate file to access functions

	def add(self,x,y):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types) and isinstance(y, number_types):
			return x + y
		else:
			raise ValueError 

	def subtract(self, x, y):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types) and isinstance(y, number_types):
			return x - y
		else:
			raise ValueError

	def multiply(self, x, y):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types) and isinstance(y, number_types):
			return x * y
		else:
			raise ValueError

	def divide(self, x, y):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types) and isinstance(y, number_types):
			if x == 0 or y == 0:
				return 'error'
			else:
				return x / y
		else:
			raise ValueError

	def exp(self, x, y):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types) and isinstance(y, number_types):
			return x ** y
		else:
			raise ValueError

	def sq(self, x,): #can only square one number 
		number_types = (int, long, float, complex)
		if isinstance(x, number_types):
			return x ** 2
		else:
			raise ValueError			
			
	def sqroot(self, x,):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types):
			return x ** (0.5)
		else:
			raise ValueError

	def sin(self, x,):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types) :			
			return math.sin(x,)
		else:
			raise ValueError

	def cos(self, x,):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types):
			return math.cos(x,)
		else:
			raise ValueError

	def tan(self, x,):
		number_types = (int, long, float, complex)
		if isinstance(x, number_types):
			return math.tan(x,)
		else:
			raise ValueError	
