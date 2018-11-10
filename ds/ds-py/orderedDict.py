from collections import OrderedDict

print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items():
	print(key, value)


print("This is a orderedDict:\n") 
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

od['b'] = 'newb'
  
for key, value in od.items():
	print(key, value)


class lastUpdatedOrderedDict(OrderedDict) :
	def __setitem__(self, key, val) :
		if key in self :
			del self[key]
		OrderedDict.__setitem__(self, key, val)



print("This is a lastupdated-orderedDict:\n") 
luod = lastUpdatedOrderedDict()
luod['a'] = 1
luod['b'] = 2
luod['c'] = 3
luod['d'] = 4

luod['b'] = 'newb'
  
for key, value in luod.items():
	print(key, value)

