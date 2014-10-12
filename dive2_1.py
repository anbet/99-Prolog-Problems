def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.
	Returns srtings."""

	return ";".join(["%s=%s" % (k,v) for k, v in params.items()])

if __name__ == "__main__":
	myParams ={"server":"mpilgrim",
	"database":"master", 
	"uid":"sa", 
	"pwd":"secret" 
	}
	 
	print buildConnectionString(myParams)

t1=type(__name__)
print t1
print buildConnectionString.__doc__

def newline():
	print
