import math

def day20():
	inputVal = 36000000
	for i in range(1, (inputVal / 10)):
		sum = 0
		root = int(i ** 0.5)
		for j in range(1, root):
			if i % j == 0:
				sum += j * 10
				sum += (i / j) * 10

		if sum >= inputVal:
			return i

print day20()

