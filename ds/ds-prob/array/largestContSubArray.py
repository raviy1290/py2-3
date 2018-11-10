def largestContSubArray(arr) :
	arr.sort()
	global_max = 1
	local_max = 1
	for i in range(1, len(arr)) :
		if arr[i] == arr[i-1] + 1 :
			local_max+=1
			global_max = max(local_max, global_max)
		else :
			local_max = 1

	print(global_max)

largestContSubArray([1, 56, 58, 57, 90, 92, 94, 93, 91, 45] )