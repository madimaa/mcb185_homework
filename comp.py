import sys

def complement(nt):
	
	if nt == 'A': return 'T'
	if nt == 'C': return 'G'
	if nt == 'G': return 'C'
	if nt == 'T': return 'A'
	sys.exit(f'unknown nucleotide {nt}')

print(complement('A'))
