import sys
filename = sys.argv[1]
def crazy(s):
	up = True
	cl = []
	for c in s:
		if up: cl.append(c.upper())
		else:  cl.append(c.lower())
		up = not up
	return ''.join(cl)
	sys.exit()

with open(filename) as fp:
	for line in fp:
		crazyline = crazy(line)
		print(crazyline)
