#10032026_MichelleCarr
#part b Calculator Functions


#1
def fahrenheit(t):
    return ((float(9)/5)*t + 32)
def celsius(t):
    return (float(5)/9*(t - 32))
def to_fahrenheit(values):
	return map(fahrenheit, values)
def to_celsius(values):
	return map(celsius, values)
    

#2
def max(values):
	return reduce(lambda a,b: a if (a>b) else b, values)

#3
def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)

#4
def add(values):
	return reduce(lambda a,b: a+b, values)

#5
def sub(values):
	return reduce(lambda a,b: a-b, values)

#6
def mul(values):
	return reduce(lambda a,b: a*b, values)

#7
def ave(values):
	return reduce(lambda a,b: (a+b)/2, values)

#8
def div(values):
	return reduce(lambda a,b: a/float(b) if (b != 0 and a != 'Nan') else 'Nan', values)

#9
def is_even(values):
	return filter(lambda x: x % 2 == 0, values)

#10
def is_odd(values):
	return filter(lambda x: x % 2 , values)

#11
def get_triplets(n):
	for x in range(1, n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

#12	
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

#test

print "Conversion to Farenheit for items in list is ", to_fahrenheit([0, 37, 40, 100])
values = to_fahrenheit([0, 37, 40, 100])
print "Conversion to Celsius for items in list is ", to_celsius(values)
print "Maximum of numbers in list = ", max([47, 11, 42, 13])	
print "Minimum of numbers in list = ", min([47, 11, 42, 13])	
print "sum of numbers in list = ", add([47, 11, 42, 13])	
print "result of subtracting consecutive numbers in list from initial value ", sub([47, 11, 42, 13])	
print "Product of items in list = ", mul([3, 5, 2, 4])
print "Show even numbers in list ", is_even([47, 12, 42, 13])	
print "average of items in list = ", ave([3, 5, 2, 6])	
print "Result of dividing by consecutive numbers in list ",  div([100, 2, 2, 5])
print "Show even numbers in list ", is_even([47, 12, 42, 13])	
print "Show odd numbers in list ", is_odd([47, 12, 42, 13])
print "see pythagorean triplets below"					
triplets = get_triplets(30)
for triplet in triplets:
	print triplet,			
print "\n"		
f = fibonacci(5) 		
print "see fibonacci range below"
for x in f:
    print x,
print	