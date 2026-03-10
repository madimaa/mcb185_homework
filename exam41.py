import sys

abc = sys.argv[1]
plus = sys.argv[2]
minus = sys.argv[3]

print('   ', end='') #starts line with space, end='' ensures line doesn't break into new line
for c in abc:
	print(c, end='  ') #prints the abc
print()

for c1 in abc:
	print(c1, end=' ') #lines 12-13 prints the lefthand column
	for c2 in abc:
		if c1 == c2: print(plus, end=' ')
		else:        print(minus, end=' ')
	print() #everything else prints the numbers in same matrix pattern