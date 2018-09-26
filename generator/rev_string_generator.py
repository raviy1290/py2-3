def rev_string(str) :
	l = len(str)
	for i in range(l-1, -1, -1) :
		yield str[i]


for c in rev_string("hello") :
	print(c)