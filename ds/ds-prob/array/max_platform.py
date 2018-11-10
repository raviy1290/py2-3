arrival = [900, 1800, 940, 950, 1100, 1500] #arrival
departure = [910, 2000, 1200, 1120, 1130, 1900] #departure

a_sort = sorted(arrival)
d_sort = sorted(departure)

trains = len(arrival) #asumption arrival departure data is right (mathinging)


cnt_platform = 0
max_platform = 0
a = 0
d = 0

while a < trains and d < trains :
	if a_sort[a] < d_sort[d] :
		cnt_platform += 1
		max_platform = max(max_platform, cnt_platform)
		a += 1
	else :
		cnt_platform -= 1
		d += 1

while a < trains :
	cnt_platform += 1
	max_platform = max(max_platform, cnt_platform)
	a += 1

while d < trains :
	cnt_platform -= 1
	d += 1	

print(max_platform)