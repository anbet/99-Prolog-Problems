def find(str1,n,ch):
	#print 'inside find'
	i=n
	while i<len(str1):
		if str1[i]==ch:
			return i		
		i=i+1
	return -1

str1= raw_input("Enter the string\n")
str1= str(str1)

#print str1

ch= raw_input("Enter character to be searched in string\n")
#print ch
n= raw_input("Enter the offset from where the search should begain\n")
n=int(n)

res= find(str1,n,ch)
if res== -1:
	print "Character not found in string\n"
else:
	print "Character found at index %d" %res
