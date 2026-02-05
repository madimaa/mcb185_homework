nts = 'ACGT'
names = 'adenine', 'cytosine', 'guanine', 'thymine'

for i in range(len(nts)):
	print(nts[i], names[i])
for nt, name in zip(nts, names):
	print(nts, name, sep='\t')
