# 1 1 2 3 5 8 13 21

a = 1
b = 1
fib = 0

while True:
	a = b
	b = fib
	fib = a + b
	print(fib)
	if fib > 100: break
