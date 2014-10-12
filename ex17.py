from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying data from %r to %r" %(from_file, to_file)


indata= (open(from_file)).read()
#Above line can be simplified into two lines------
#infile=open(from_file)
#indata= infile.read()

print "The content of the file is %d bytes long" % len(indata)
print "Does the to_file exists? %r" % exists(to_file)

print "To abort the run PRESS CLTR+Z"
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "We are ready to go!"

out_file.close()





