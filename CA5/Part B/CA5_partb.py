add = lambda x,y: x+y
print add(10,101)

subtract = lambda x,y: x-y
print subtract(101,10)

multiply = lambda x,y: x*y
print multiply(101,10)



fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
print fibonacci
result = filter(lambda x: x % 2, fibonacci)
print result

result = filter(lambda x: x % 2 == 0, fibonacci)
print result

def fibonacci_lst(n):

    a = 0
    b = 1
    counter = 0
    while True:
        if (counter >= n): return
		
        yield a
        c = a
        a = b
        b = c + b
        counter += 1
f = fibonacci_lst(20)
for x in f:
    print x,
print



def pythagorean(n):
    for x in range(1,1000): #1000 takes a few seconds to run, N takes ages 
	for x in range(1,1000): #1000 takes a few seconds to run, N takes ages 
		for y in range(x,1000):
			for z in range(y,1000):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

pyt = pythagorean(3000)
for v in pyt:
    print v,