def fact(n):
	if n==0:
		return 1
	else:
		i=2
		while i<=n:
			i=i*(i-1)
			i+=1
		return i

n1=raw_input("Enter the number\n")
n1=int(n1)
n2=fact(n1)
print n2

