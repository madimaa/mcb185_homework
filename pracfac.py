import math

def factorial(n):
	total = 1
	for i in range(1, n+1):
		total = total * i
	return total

print(factorial(5))

prev = -1
e = 0
i = 0

while True:
	e = e + 1/factorial(1)
	i += 1
	print(i,e)
	if abs(e > prev) < 1e-6: break
	prev = e
