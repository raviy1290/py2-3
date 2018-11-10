def sol(digit, l) :
	#l is length of array in question 
	# would go from len(digit) to 0

	if l == 0 or l == 1:
		return 1

	if digit[-l] == 0 :
		return 0


	if digit[-l+1] + 10*digit[-l] > 26 :
		return sol(digit, l-1)
	else :
		if digit[-l+1] == 0 :
			return sol(digit, l-2)
		return sol(digit, l-1) + sol(digit, l-2)

def sol2(digit, start) :
	#start is start index for target arry 
	#would vary from 0, len(digit)-1

	if start == len(digit)-1 or start == len(digit) :
		return 1

	if digit[start] == 0 :
		return 0


	if digit[start]*10 + digit[start+1] > 26 :
		return sol2(digit, start+1)
	else :
		if digit[start+1] == 0 :
			return sol2(digit, start+2)
		return sol2(digit, start+1) + sol2(digit, start+2)

def countPossibleDecoding(digits) :
	print(sol(digits, len(digits)))
	print(sol2(digits, 0))


arr = [1, 2, 3, 4]
arr1 = [1, 0, 2, 2, 1]
countPossibleDecoding(arr1)


