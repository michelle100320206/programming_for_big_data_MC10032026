import math
import calccode


class uimathcalc(object):	#class for ui function 
	mycalc = calccode.mathcalc()#reference calccode functions

	print "1: ADDITION"
	print "2: SUBTRACTION"
	print "3: MULTIPLICATION"
	print "4: DIVITION"
	print "5: EXPONENT"
	print "6: SQUARED"
	print "7: SQROOT"
	print "8: SINE"
	print "9: COSINE"
	print "10: TANGENT"
	print "0: QUIT"

	while True:
		CHOICE = int(raw_input("ENTER THE CORRESPONDING NUMBER FOR CALCULATION ")) 

		if CHOICE == 1: 
			print 'ADDING TWO NUMBERS:'
			print "Enter the two numbers to Add"
			X=float(raw_input("Enter X: "))#input from users - take in as str make float so function works -number types defined in functions
			Y=float(raw_input("Enter Y: "))
			result = mycalc.add(X,Y)
			print result

		elif CHOICE == 2:
			print 'SUBTRACTING TWO NUMBERS::'
			print "Enter the two numbers to Subtract"
			X=float(raw_input("Enter X: "))
			Y=float(raw_input("Enter Y: "))
			result = mycalc.subtract(X,Y)
			print result #should have looked for different print statement _return or the likes_too many prints in loop make code difficult to read




		elif CHOICE == 3:
			print 'Multplying TWO NUMBERS:'
			print "Enter the two numbers to mutiply"
			X=float(raw_input("Enter X: "))
			Y=float(raw_input("Enter Y: "))
			result = mycalc.multiply(X,Y)
			print result
			print 'its working so far'


		elif CHOICE == 4:
			print 'Dividing TWO NUMBERS:'
			print "Enter the two numbers to divide"
			X=float(raw_input("Enter X: "))
			Y=float(raw_input("Enter Y: "))
			result = mycalc.divide(X,Y)
			print result


		
		elif CHOICE == 5:
			print 'EXPONENT OF TWO NUMBERS:'
			print "Enter the two numbers to exponent"
			X=float(raw_input("Enter X: "))
			Y=float(raw_input("Enter Y: "))
			result = mycalc.exp(X,Y)
			print result

		
		elif CHOICE == 6:
			print 'SQUARE OF ONE NUMBER:'
			print "Enter the one number to square"
			X=float(raw_input("Enter X: "))
			result = mycalc.sq(X,)
			print result
			print 'its working so far'
		

		elif CHOICE == 7:
			print 'SQUAREROOT OF ONE NUMBER:'
			print "Enter the one number to sqroot"
			X=float(raw_input("Enter X: "))
			result = mycalc.sqroot(X,)
			print result
	
			
		elif CHOICE == 8:
			print 'SINE OF ONE NUMBER:'
			print 'Enter one number to return the sine of X in radians.'
			X=float(raw_input("Enter X: "))
			result = mycalc.sin(X,)
			print result

		
			
		elif CHOICE == 9:
			print 'COSINE OF ONE NUMBER:'
			print 'Enter one number to return the cosine of X in radians.'
			X=float(raw_input("Enter X: "))
			result = mycalc.cos(X,)
			print result

		
			
		elif CHOICE == 10:
			print 'TANGENT OF ONE NUMBER:'
			print 'Enter one number to return the tangent of X in radians.'
			X=float(raw_input("Enter X: "))
			result = mycalc.tan(X,)
			print result
			print 'its working so far'	
		
			
		elif CHOICE == 0: #exit option from loop
			print "Thank you for choosing Michelles scientific calculator Have a nice day"
			exit()
		else:
			print "Error please enter a valid numerical selection from 1-10" #reject any other value apart from 1-10.

	
	
if __name__ == '__main__':
    unittest.main()
	
# C:\Users\carrm\Desktop\CA1>calcui.py
# 1: ADDITION
# 2: SUBTRACTION
# 3: MULTIPLICATION
# 4: DIVITION
# 5: EXPONENT
# 6: SQUARED
# 7: SQROOT
# 8: SINE
# 9: COSINE
# 10: TANGENT
# 0: QUIT
# ENTER THE CORRESPONDING NUMBER FOR CALCULATION