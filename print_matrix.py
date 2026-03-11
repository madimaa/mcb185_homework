import sys
seq = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3] #no need to convert into numbers we wont use them as numbers

"""

show_matrix.py ACGT +2 -1

     A  C  G  T
A   +2 -1 -1 -1
C	-1 +2 -1 -1
G	-1 -1 +2 -1
T	-1 -1 -1 +2

"""
#print header line, there's just one
print('   ', end='')
for nt in seq: print(nt, end='   ')
print()
"""
for nt1 in seq:
	print(nt1, end=' ')
	for nt2 in seq:
		if nt1 == nt2: print(mat, end='  ')
		else:          print(mis, end='  ')
	print()
"""

for i in range(0, len(seq)):
	print(seq[i], end=' ')
	for j in range(0, len(seq)):
		if seq[i] == seq[j]: print(mat, end='  ')
		else:                print(mis, end='  ')
	print()
	
