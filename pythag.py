def hypotenuse(a, b):
	c = (a**2 + b**2)**0.5
	return c

for a in range(1, 5):
	for b in range(1, 5):
		print('pythagoreon', hypotenuse(3, 4))
