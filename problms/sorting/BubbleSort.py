def bubbleSort(ulist) :
	len_list = len(ulist)
	'''
		move largest elem at the end of list
		by exchanging two at a time
	'''
	for pass_number in range(len_list) :
		for j in range(1, len_list-pass_number) :
			if ulist[j-1] > ulist[j] :
				ulist[j-1] , ulist[j] = ulist[j], ulist[j-1]

# blist = [64, 34, 25, 12, 22, 11, 90]
# print(blist)
# bubbleSort(blist)
# print(blist)


def bubbleSortOpt(ulist) :
	is_exchange = True
	pass_num = len(ulist)

	while pass_num > 0 and is_exchange :
		is_exchange = False

		for j in range(1, pass_num) :
			if ulist[j] < ulist[j-1] :
				is_exchange = True
				ulist[j-1] , ulist[j] = ulist[j], ulist[j-1]

		if not is_exchange :
			break

# blist = [64, 34, 25, 12, 22, 11, 90]
# print(blist)
# bubbleSortOpt(blist)
# print(blist)


def bubbleToSelectionSort(ulist) :
	'''
	Bubble to Selection 
	in one loop only one exchange - 
	move max to right 
	'''
	len_list = len(ulist)

	for pass_number in range(len_list) :
		
		max_idx = 0

		for j in range(1, len_list-pass_number) :
			if ulist[j] > ulist[max_idx] :
				max_idx = j

		ulist[max_idx], ulist[len_list-pass_number-1] = ulist[len_list-pass_number-1], ulist[max_idx]

blist = [64, 34, 25, 12, 22, 11, 90]
print(blist)
bubbleToSelectionSort(blist)
print(blist)