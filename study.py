import math
e = 0
for i in range(1,200):
	e = e + 1/math.factorial(i)
	print(e)
	if e == e+1/math.factorial(i): break
