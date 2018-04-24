x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

ab = (x1 - x2) ** 2 + (y1 - y2) ** 2
ac = (x1 - x3) ** 2 + (y1 - y3) ** 2
bc = (x2 - x3) ** 2 + (y2 - y3) ** 2

if ab == bc + ac or bc == ab + ac or ac == ab + bc:
	print('yes')
else:
	print('no')