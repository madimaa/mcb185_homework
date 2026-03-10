#pythagorean triple: 3, 4, 5 - 3^2 + 4^2 = 5^2
stuff = ('A', 'B', 'C', 'D')
for i in range(len(stuff)):
	for j in range(i+1, len(stuff)): #i and j = integers var. use them when using range
		print(i, j)