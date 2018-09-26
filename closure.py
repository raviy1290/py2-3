def outer(o) :
	def inner(i) :
		return o+i
	return inner

x = outer(5)

print(type(outer))
del(outer)

try :
	print(type(outer))
except NameError as e:
	print(e)

print(x(4))