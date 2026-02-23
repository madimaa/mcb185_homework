import random

outside = 1
inside = 1
while True:
	x = random.random()
	y = random.random()
	d = (x**2 + y**2)**0.5
	if d > 1: outside +=1
	else: inside += 1
	print(4 * inside / (inside+outside))
	
# fun test Q variant

