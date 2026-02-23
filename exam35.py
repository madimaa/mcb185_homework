def hydropathy(seq):
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, 
		-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
	
	total = 0
	for aa in seq:
		idx = aas.index(aa)
		print(aa, idx)
		total += kdh[idx]
	return total / len(seq)
		
print(hydropathy('M'))
