def findMaxTrappedWater(arr, n): 

	left = [0]*n
	right = [0]*n

	left[0] = arr[0]
	right[-1] = arr[-1]
	water = 0

	for i in range(1, n) :
		left[i] = max(left[i-1], arr[i])

	for i in range(n-2, -1, -1) :
		right[i] = max(right[i+1], arr[i])

	print(left)
	print(right)

	for i in range(1, n) :
		water += min(left[i], right[i]) - arr[i]

	print(water)
  
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr = [5, 1, 2, 8, 1, 2, 7] 
n = len(arr)
findMaxTrappedWater(arr, n)



def findMaxTrappedWaterPossible(arr, n): 
	#assuming all the waals inbtw can be collaspsible


















# def unique(s):
#     i, j = 0, 0
#     I, J = 0, 0
#     H = set([])
#     while j < len(s):
#         if s[j] in H:
#             H.remove(s[i])
#             i += 1
#         else:
#             H.add(s[j])
#             j += 1
#         if J - I < j - i:
#             I, J = i, j
#     return s[I:J]
# print(unique('babacda')) # bacd


