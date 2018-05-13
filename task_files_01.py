
n = int(input('Введите число n: '))
p = int(input('Введите число p: '))


with open('data.txt') as f:
	data = f.read()
	out1 = []
	out2 = []
	for value in data.split(' '):
		if int(value) % n == 0:
			out1.append(value)
		out2.append(int(value) ** p)


with open('out-1.txt', 'w') as f:
	f.write(' '.join(out1))

with open('out-2.txt', 'w') as f:
	f.write(' '.join(str(value) for value in out2))

	
