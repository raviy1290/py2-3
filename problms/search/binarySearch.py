def bsUtil(a, f, start, end) :
	if end >= start :
		mid = (start+end)//2

		print(start, end, mid)

		if f == a[mid] :
			print("found", f, a[mid])
			return mid
		elif f > a[mid] :
			return bsUtil(a, f, mid+1, end)
		else : 
			return bsUtil(a, f, start, mid-1)
	else :
		return -1

def binarySearch(arr, x) :
	result = bsUtil(arr, x, 0, len(arr)-1)
	print(result)

arr = [2, 3, 4, 10, 40]
x =10
binarySearch(arr, x)

