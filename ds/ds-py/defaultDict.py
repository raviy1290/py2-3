from collections import defaultdict

dd = defaultdict(int)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

for k, v in s :
	dd[k]+=v

print(dd)

