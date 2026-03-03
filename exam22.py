import sys

seq = sys.argv[1]
def tm(s):
	s = s.upper()
	a = s.count('A')
	c = s.count('C')
	g = s.count('G')
	t = s.count('T')
	if len(s) != a + c + g + t: sys.exit('error in sequence')
	if len(s) <= 13:
		return (a + t) * 2 + (c + g) * 4
	else:
		return 64.9 + 41 * (c+g-16.4)/(a+c+g+t)

print(tm(seq))


