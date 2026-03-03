def anti(dna):
	dna = dna.upper()
	comp = list() #list() = [] both make empty list
	for nt in dna:
		if nt == 'A': comp.append('T')
		elif nt == 'C': comp.append('G')
		elif nt == 'G': comp.append('C')
		elif nt == 'T': comp.append('A')
		else: sys.exit(f'unknown nt {nt}')
	return ''.join(comp)
seq = input('type sequence: ')
print(seq)
print(anti(seq))
