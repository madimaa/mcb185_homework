def manhattan(X1, X2):
	distance = 0
	for x1, x2 in zip(X1, X2):
		distance += abs(x1 - x2)
	return distance
	
a = [0.4, 0.3, 0.2, 0.1]
b = [0.4, 0.3, 0.2, 0.1]

print(manhattan(a, b))