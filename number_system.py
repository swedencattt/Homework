def dec2bin(number):
	system = 2
	return from_dec(number, system)
def dec2oct(number):
	system = 8
	return from_dec(number, system)
def dec2hex(number):
	system = 16
	return from_dec(number, system)
def bin2dec(number):
	system = 2
	return to_dec(number, system)
def oct2dec(number):
	system = 8
	return to_dec(number, system)
def hex2dec(number):
	system = 16
	return to_dec(number, system)

def to_dec(number, system):
	result = 0
	number = number[::-1]
	letters = 'abcdef'
	for i in range(len(number)):
		if number[i] in letters:
			result += int(letters.index(number[i]) + 10) * system ** i
		else:
			result += int(number[i]) * system ** i
	return result


def from_dec(number, system):
	res = ''
	result = res[::-1]
	letters = 'abcdef'
	while number > 1:
		if number % system > 9:
			res += str(letters[(number % system)] - 10)
		else:
			res += str(number % system)
	return result

