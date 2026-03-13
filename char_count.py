import sys
filename = sys.argv[1]

char_count = [0] * 128
with open(filename) as fp:
	for line in fp:
		for c in line:
			asci = ord(c)
			char_count[asci] += 1
for asci in range(128):
	if asci <= 32: print(asci, char_count[asci])
	else: print(chr(asci), char_count[asci])
