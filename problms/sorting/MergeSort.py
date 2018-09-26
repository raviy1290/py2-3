def mergeSort(unsorted_list) :
	if len(unsorted_list) <= 1 :
		return unsorted_list

	middle = len(unsorted_list) // 2 #flooring

	left_list = mergeSort(unsorted_list[:middle])
	right_list = mergeSort(unsorted_list[middle:])

	return merge_sorted_lists(left_list, right_list)

def merge_sorted_lists(left, right) :
	res = []

	while len(left) > 0 and len(right) > 0 :
		if left[0] < right[0] :
			res.append(left[0])
			left.remove(left[0])
		else :
			res.append(right[0])
			right.remove(right[0])

	if len(left) > 0 :
		res += left

	if len(right) > 0 :
		res += right

	return res

mlist = [64, 34, 25, 12, 22, 11, 90]
print(mergeSort(mlist))	
