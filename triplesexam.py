import sys
maxnum = int(sys.argv[1])
for a in range(0, maxnum):
	for b in range(a+1, maxnum):
		c = (a**2 + b**2)**0.5
		if c % 1 == 0: 
			print(a, b, c)
