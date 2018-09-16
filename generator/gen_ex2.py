def func() :
	print("printing or not")
	exit()
	yield

# x = func()
# print(type(x))

# returns generator type 

def one_to_ten() :
	val = 1
	while val <= 10 :
		yield val
		val += 1

x = one_to_ten() # return a generator as YIELD is used 

nx = next(x)
while nx :
	print(nx)
	nx = next(x)

# 	function vs generators
#	subroutines vs co routines 
#	return vs yield
#	control of execution -local var/states - freah vs retaining 

