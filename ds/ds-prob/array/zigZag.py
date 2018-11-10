def zigZag(arr, l, flag) :
	flag = flag # means increading else deceeasing
	for i in range(l-1) :
		if flag :
			if arr[i] > arr[i+1] :
				arr[i], arr[i+1] = arr[i+1], arr[i]
		else :
			if arr[i] < arr[i+1] :
				arr[i], arr[i+1] = arr[i+1], arr[i]

		flag = not flag

	print(arr)

zigZag([4, 3, 7, 8, 6, 2, 1], 7, True)

zigZag([4, 3, 7, 8, 6, 2, 1], 7, False)
