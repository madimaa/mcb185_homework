import sys

def anti(dna):
	rev = dna[::-1]
	comp = list()
	for nt in rev:
		if nt == 'A': comp.append('T')
		elif nt == 'C': comp.append('G')
		elif nt == 'G': comp.append('C')
		elif nt == 'T': comp.append('A')
		else: sys.exit(f'unknown nt {nt}')
	return ''.join(comp)

seq = input('type sequence: ')
print(seq)
print(anti(seq))
