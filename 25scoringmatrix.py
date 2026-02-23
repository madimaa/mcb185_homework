import sys

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]
# print header
print('  ', end='  ')
for c in alph:
	print(c, end='  ')
print()
#print full matrix, leading with letter
for i in range(len(alph)):
	# print leading letter
	print(alph[i], end='  ')
	# print row
	for j in range(len(alph)):
		if i == j: print(mat, end=' ')
		else:  print(mis, end=' ')
	print()
	