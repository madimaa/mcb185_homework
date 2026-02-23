import sys

def get_list_from_file(filename):
	strings = []
	with open(filename) as fp:
		for line in fp:
			strings.append(line.rstrip())
	return strings

def jaccard(f1, f2):
	X1 = get_list_from_file(f1)
	X2 = get_list_from_file(f2)
	unique_a = []
	unique_b = []
	shared = []
	for x1 in X1:
		if x1 in X2: shared.append(x1)
		else:        unique_a.append(x1)
	for x2 in X2:
		if x2 not in X1: unique_b.append(x2)
	print(unique_a)
	print(unique_b)
	print(shared)
	return len(shared) / (len(shared) + len(unique_a) + (unique_b))
	
file1 = sys.argv[1]
file2 = sys.argv[2]

print(jaccard(file1, file2))