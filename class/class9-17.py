# Class Sept. 17, 2012

# def max(a, b, c):
# 	if a>b and a>c:
# 		return a
# 	elif b>c:
# 		return b
# 	return c

'''short circuit evaluation'''
# number = 6
# x = 3
# if x != 0 and number % x == 0:
# 	print number, "is divisible by", x

'''generating random numbers'''
import random

# random.randrange(1,100)		#gives you "random" number 1-100, not including 100
# 
# random.seed(5)				#re-seed random number generator. seed = first number in sequence

'''using random numbers to approximate pi'''
import random
import math							#import to use "square root" function
def MontePi(numDarts):
	inCircle = 0.0
	for dart in range(numDarts):
		x = random.random()			#random.random() gives you random numbers between 0 and 1
		y = random.random()
		
		if math.sqrt(x ** 2 + y ** 2) <= 1:
			inCircle = inCircle +1
	return (inCircle / numDarts) * 4
print MontePi(10000)