import sys
import re
import random

def driver(inputs) :
	out = validate_input(inputs)
	return calculate_result(out)


def validate_input(inputs) :
	#validate each input 
	for i in inputs :
		if i.isnumeric() or i in['d', 'D'] :
			print("Invalid Input")
			sys.exit()

	input_str = ''.join(inputs)
	input_str = input_str.upper()
	output = re.findall('([+|-]*\d+D\d+)', input_str)

	for elem in output :
		tokens = elem.split("D")
		if int(tokens[-1]) not in ALLOWED :
			print("dice with face",  tokens[-1], "not allowed")
			sys.exit()

	return output

# calculation for results 
def calculate_result(output) :
	result = 0
	for elem in output :
		tokens = elem.split("D")

		if elem[0] == '+' :
			result += int(tokens[0][1:])*random.randint(1, int(tokens[-1]))
		elif elem[0] == '-' :
			result -= int(tokens[0][1:])*random.randint(1, int(tokens[-1]))
		else :
			result += int(tokens[0])*random.randint(1, int(tokens[-1]))

	return result


# allowed dices faces
ALLOWED = (4, 6, 8, 10, 12, 20)
inputs = sys.argv[1:]
print(driver(inputs))