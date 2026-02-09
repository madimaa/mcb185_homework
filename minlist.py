def minimum(values):
	my_min = x[0]
	my_max = x[0]
	for value in values[1:]:
		if value < my_min: my_min = value
		if value > my_max: my_max = value
	return my_min, my_max
		
x = [3.14, 2.79, 1/7, 0, -2, 1]
a, b = minimum(x)
print('min', a)
print('max', b)

for pos, val in enumerate(x):
	print(val, pos)
