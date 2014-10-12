def c_and_c(cheese_count, boxes_of_crackers):
	print "you have %d cheese!"% cheese_count
	print "you have %d box of crackers!"% boxes_of_crackers
	print "Man thats enoughf for a party!"
	print "Get a blackent.\n"

def greetings(greet):
	print "Hello %r wellcome to Axionet."% greet
	print "We make world smart at Axionet."
	print "We take the privilage to have u, %r\n"% greet

print "We start the function dirctly by giving the numbers!"
c_and_c(10, 20)

print "Now we use the variables from the script\n"
cheese=30
crackers=40
c_and_c(cheese,crackers)

print "We can do maths inside it too"
c_and_c(10+20+30,30+20)

print "We combine the variables and the numbers"
c_and_c(cheese+100,crackers+100)

greetings(004+004)
greetings("""zed""")
