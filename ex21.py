def add(a, b):
	print "Adding..... %d + %d"% (a,b)
	return a+b

def substract(a, b):
	print "Substracting.... %d - %d"% (a,b)
	return a-b

def multiply(a, b):
	print "Multiply..... %d*%d"% (a,b)
	return a*b

def divide(a, b):
	print "Dividing.... %d/%d"% (a,b)
	return a/b

print "Lets do some Math!"

age = add(50, 5)
height= substract(78, 4)
weight= multiply(90, 2)
iq = divide(100,2)

print " Age: %d\n Height: %d\n Weight: %d\n Iq=%d\n"% (age,height,weight,iq)

# A puzzle for the extra credit , type it in anyway.

print "Here is a puzzle."

what= add(age, substract(height, multiply(weight, divide(iq, 3))))
what1=float(what)

print "That becomes:",what1,"can you do it by hand?"

