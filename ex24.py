print "Lets practice everthing."
print "You\'d need to know \ 'bout escapes with \\ that do \n newlines that do \n newlines and \t tabs."

poem= """
\t The lover world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from instuition 
and requries an explination
\n\t\t where there is none."""

print "-----------------"
print poem
print "-----------------"

five = 10 - 2 + 3 - 5
print "This should de five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

print "With a starting point of: %d" % (jelly_beans, jars, crates)
print "We'd have %d beans, %d jars, and %d crates."% secret_formula(start_point=3.3)

