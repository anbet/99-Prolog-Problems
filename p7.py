#This is butifull example illustrating the Reccursion, extend and append

def flat_list(li):
	res=[]
	for el in li:
		if type(el) is list:
			res.extend(flat_list(el))
		else:
			res.append(el)
	return res

if __name__=="__main__":
	li=[['a',['b',['c','d'],'e'],'f']]
	v0=flat_list(li)
	print v0
			
