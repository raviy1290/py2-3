def findPithagorus(arr, n) :
	arr.sort()
	print(arr, len(arr), n)

	for i in range(n-1, 1, -1) :
		j = 0
		k = i-1

		while (j < k ) :
			print(arr[j], arr[k], arr[i])
			if arr[i]**2 == (arr[j]**2 + arr[k]**2) :
				return arr[j], arr[k], arr[i]
			else :
				if arr[i]**2 > (arr[j]**2 + arr[k]**2) :
					#reduce k
					j = j+1
				else :
					k = k-1
	return False

print(findPithagorus([1, 3 , 4, 5, 6], 5))


