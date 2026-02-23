import itertools

def translate(seq):
	codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
	trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
	
	protein = ''
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]	
		idx = codons.index(codon)
		aa = trans[idx]
		protein += aa
		#print(codon, idx, aa)
	return protein
		
seq = 'ATGGTGTAA'

print(translate(seq))
