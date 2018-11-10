def maxStocksVal(A) :
	index = 0
	ranges = {}
	ranges[index] = list()
	ranges[index].append(0)
	
	for i in range(1, len(A)) :
		if A[i] < A[i-1] and A[i] < A[i+1]:

			# Ai is local minima
			index += 1
			ranges[index] = list()
			ranges[index].append(i)
		
		elif  A[i] > A[i-1] :
			ranges[index].append(i)
		else :
			pass
			

	print(ranges)



arr = [100, 180, 260, 310, 40, 535, 695]

arr = [100, 180, 260, 310, 300, 400, 300, 40, 535, 695]

maxStocksVal(arr)