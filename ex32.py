the_count=[1,2,3,4,5]
fruits=["Mango","Banana","orange","apple"]
change=[1,"Pennies",2,"dimes",3,"quarters"]

for number in the_count:
	print "The count %d:" % number

for fruit in fruits:
	print "The fruits so type %s " % (fruit)

for i in change:
	print "I got %r"% i

elements=[]

for i in range(0,6):
	print "Adding element to %d list" % i
	elements.append(i)

for i in elements:
	print "Elements in list are:"
	print i
