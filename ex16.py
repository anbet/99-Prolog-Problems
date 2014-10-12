from sys import argv

script, filename= argv

print "1 We are going to erase %r"% filename
print "1 If you dont want that, hit CLTR-c."
print "1 If you do want that , hit RETURN."

raw_input("?")

print "Opening the file...."
target= open(filename,'w')

print "Truncating the file. Goodbye!"
#target.truncate()     # truncated--- If the file is created, the content is deleted and new data is printed

#if we use the write in the open, truncate is not require truncate option.

print "Now I'm going to ask you for there lines."

line1= raw_input("lines 1:")
line2= raw_input("lines 2:")
line3= raw_input("lines 3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "And finally , we close it."
target.close()
