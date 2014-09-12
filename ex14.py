from sys import argv

script, user_name= argv
prompt = '> '

print "Hi %s, I'm the %s script"% (user_name, script)
print "I'd like to ask you a few Questions. "

print "Do you like me %s"%user_name
likes= raw_input(prompt)

print "Where do you live %s "%user_name
lives= raw_input(prompt)

print "What Kind of computer do you have?"
compuer= raw_input(prompt)
 
print """
Alright, so you said %r about liking me.
you live in %r. Not sure Where that is.
And you have a %r coumputer. Nice.
"""% (likes, lives, co)
