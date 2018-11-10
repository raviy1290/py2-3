def quickSort(ulist) :
	quickSortHelper(ulist, 0, len(ulist)-1)
	#both left, right are valid list points

def quickSortHelper(ulist, first, last) :
	if first < last :
		split_point = partition(ulist, first, last)
		quickSortHelper(ulist, first, split_point-1)
		quickSortHelper(ulist, split_point+1, last)

def partition(ulist, f, l) :
	#both f, l are valif list points 
	pivot = ulist[f]

	left_mark = f+1
	right_mark = l

	done = False
	while not done :
		while left_mark <= right_mark and ulist[left_mark] <= pivot :
			left_mark +=1 

		while left_mark <= right_mark and ulist[right_mark] >= pivot :
			right_mark -=1 

		if right_mark < left_mark :
			done = True
		else :
			ulist[left_mark], ulist[right_mark] = ulist[right_mark], ulist[left_mark]

	ulist[f], ulist[right_mark] = ulist[right_mark], ulist[f]
	print(ulist)
	return right_mark

ulist = [54,26,93,17,77,31,44,55,20]
quickSort(ulist)
print(ulist)