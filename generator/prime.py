# 	function vs generators
#	subroutines vs co routines 
#	return vs yield
#	control of execution -local var/states - freah vs retaining 

import time

def get_ps(input_list) :
	res_list = list()
	for elem in input_list :
		if is_p(elem) :
			res_list.append(elem)

	return res_list


def is_p(num) :
	if num > 1 :
		if num == 2:
			return True

		if num % 2 == 0 :
			return False 

		for current in range(3, int(num** 0.5) + 1) :
			if num % current == 0 :
				return False 
		return True

	return False


def get_ps_gen(input_list) :
	return ( n for n in input_list if is_p(n))


n = 100000

print(time.ctime())
print(get_ps(range(n)))
print(time.ctime())

print(time.ctime())
print(get_ps_gen(range(n)))
print(time.ctime())