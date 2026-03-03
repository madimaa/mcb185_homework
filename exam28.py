def minmax(vals):
	a = vals[0]
	b = vals[0]
	for val in vals[1:]:
		if val < a: a = val
		if val > b: b = val
	return a, b
s = [1, 2, 3, 4, 10]
print(minmax(s))
