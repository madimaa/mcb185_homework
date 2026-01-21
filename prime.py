def is_prime(n):
	for i in range(3, n):
		print('checking', i)
		r = n % i
		if r == 0: return False
		print(n, 'divided by', i, n / i )
	return True

print(is_prime(3103))
