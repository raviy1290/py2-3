d = dict(one=1, two=2)

d['1'] = 'one'
d['2'] = 'two'
d['one'] = 11

print(d)

iter = iter(d)

while True :
	try :
		print(next(iter))
	except StopIteration:
		break

print(d.popitem())
print(d.popitem())