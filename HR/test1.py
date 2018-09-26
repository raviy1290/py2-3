# cnt_num = input()
# nums = list(map(int, input().split()))

# if int(cnt_num)==len(nums) :
# 	for n in nums :
# 		for i in range(1, n+1) :
# 			if i % 3 == 0 and i % 5 == 0 :
# 				print("FizzBuzz")
# 			elif i % 3 == 0 :
# 				print("Fizz")
# 			elif i % 5 == 0 :
# 				print("Buzz")
# 			else :
# 				print(i)


# class M(object) :
# 	def __init__(self, p) :
# 		self.p1=p

# class C(M) :
# 	def __init__(self, p):
# 		self.p2=p

# obj = C(22)
# print(obj.p1, obj.p2)

def foo():
	try :
		return 1
	except :
		return 2

z = foo()
print(z)
