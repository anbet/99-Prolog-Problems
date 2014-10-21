import string
def uncompress(li):
	res=[]
	v0=[]
	res1=[]
	 
	for e in li:
		if type(e) is list:  
			res.extend(e)
			print res,"inside extend"
		else:
			res.append(e)
			print res, "inside append"

	print res,'the result '

	for i,e1 in enumerate(res[:-1]):
		print string.digits

		if e1 in string.digits:
			#print string.digits

			temp=res[i-1]*int(res[i])
			print temp,'the temp'
			v0.append(temp )
		else:
			v0.append(e1)  
	#print res
	return v0
	 

if __name__=="__main__":
	li=[['a', '2'], ['b', '2'], 'c', 'd', ['a', '3'], 'b', 'c', 'd', 'e']
	v0=uncompress(li)
	print v0	
