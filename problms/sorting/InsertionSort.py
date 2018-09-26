def insertionSort(unsorted_list) :
	len_list = len(unsorted_list)
	'''
		inseration sorting -
		for item at index i in list
		keep it in order in list[:i-1]
		?
	'''
	for index in range(1, len_list) :

		current_val = unsorted_list[index]
		current_pos = index 

		# optimization - this part can be done binary ln(n)
		# complexity would come down O(n**2) to O(nlogn)

		while current_pos > 0 and unsorted_list[current_pos-1] > current_val :
			unsorted_list[current_pos] = unsorted_list[current_pos-1]
			current_pos -= 1
		unsorted_list[current_pos] = current_val

		print("loop-", index, unsorted_list)

ilist = [64, 34, 25, 12, 22, 11, 90]
print(ilist)
insertionSort(ilist)
print(ilist)



