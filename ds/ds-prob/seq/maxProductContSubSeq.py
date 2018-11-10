import math
def maxProduct(arr) :

	max_product_till_i = 1
	min_product_till_i = 1

	overall_max_product = 1

	for i in range(len(arr)) :

		print(i, max_product_till_i, min_product_till_i, overall_max_product)

		if arr[i] > 0 :
			max_product_till_i = max_product_till_i*arr[i]
			min_product_till_i = min(min_product_till_i*arr[i], 1)	

		if arr[i] < 0 :
			temp = max_product_till_i
			max_product_till_i = max(1, min_product_till_i*arr[i])
			min_product_till_i = max_product_till_i*arr[i]	

		if arr[i] == 0 :
			max_product_till_i = 1
			min_product_till_i = 1	

		if 	max_product_till_i > overall_max_product :
			overall_max_product = max_product_till_i

	print(overall_max_product)

maxProduct([-30, -20, 0 , 1])	