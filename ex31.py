print "You enter a dark room with two doors. Do you go through door"

door = raw_input("> ")

if door == '1':
	print "There's a gaint bear here eating a cheese cake. what do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	
	if bear=="1":
		print "Bear eats your face off. Good job"
	elif bear=="2":
		print "Bear eats your legs off."
	else:
		print"Well, doing %s is probably  better. Bear runs away" % bear

elif door== '2':
	print "You stare at the endless abyss at cthulhu's retina."
	print "1: Bluberries."
	print "2: yellow jacket clothspins."
	print "3. Understand resolver yelling melodies"

	insanity = raw_input("> ")
	
	if insanity == '1' or insanity == '2':
		print "Your body survives powered by the mind of jello. Good job."
	else:
		print "The insanity rots your eyes into pool of muck. good job!"
else :
	print "You stumbed"

