f = []
s = []

n = 7

used = 0 
time = 0

while True :
	if f is None and s is None :
		f.append(1)
		s.append(0)

		time += 1
		used += 1
		continue

	if used == n :
		time += 5
		break

	if len(f) == 5 and len(s) == 5 :
		f.pop(0)
		s.pop(0)

	if sum(f) == sum(s) :
		f.append(1)
		s.append(0)

		time += 1
		used += 1
		continue

	if sum(f) - sum(s) == 1 :
		s.append(1)
		f.append(0)

		time += 1
		used += 1
		continue
	else :
		f.append(1)
		s.append(0)

		time += 1
		used += 1
		continue

print(time)








