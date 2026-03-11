import sys
import math
def entropy(seq):
	pa = seq.count('A') / len(seq)
	pc = seq.count('C') / len(seq)
	pg = seq.count('G') / len(seq)
	pt = seq.count('T') / len(seq)
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h
print(entropy('ACGTAAAACGT'))

def dust(seq, w, t):
	eseq = list(seq)
	for i in range(len(seq) -w+1):
		win = seq[i:i+w]
		if entropy(win) < t:
			for j in range(i, i+w): 
				eseq[j] = seq[j].lower()
	return ''.join(eseq)
		
print(dust('ACGTAAAAACGT', 6, 1.1))