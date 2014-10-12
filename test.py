def multi(n):
	i=1
	
	while i<=n:
		j=1
		while j<=i:
			print i*j,"\t",
			j+=1
		print
		
		i+=1

n1=raw_input("Enter the number to find tabels upto\n")
n1=int(n1)
multi(n1)



	
