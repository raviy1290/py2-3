def maxSumContSubSeq(arr) :

	max_sum_s_far = 0
	max_sum_ending_here = 0
	for i in range(len(arr)) :
		print(max_sum_ending_here, max_sum_s_far)
		max_sum_ending_here += arr[i]

		if max_sum_ending_here <= 0 :
			max_sum_ending_here = 0

		else :
			max_sum_s_far = max(max_sum_s_far, max_sum_ending_here)

	print(max_sum_s_far)	


maxSumContSubSeq([1, 2, -5, 6, 8, -15, 1, 6, 10])		
