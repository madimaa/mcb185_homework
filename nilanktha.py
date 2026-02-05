def nilakantha(x):
	pi = 3
	for i in range(1, x+1):
		n = 2 * i
		d = n * (n+1) * (n+2)
		if i % 2 == 0: pi = pi - 4 / d
		else:          pi = pi + 4 / d
	print(pi)
	if pi == 3.141592: break
print(nilakantha(100))	
