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

def get_ps(number):
	while True:
		print("IN", number)
		if is_p(number):
			number = yield number
		number += 1

def print_ps_iteration(iterations, base=10):
    prime_generator = get_ps(base)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(base ** power))


print_ps_iteration(4 , 10)