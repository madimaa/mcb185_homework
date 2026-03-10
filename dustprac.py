import math

#entropy func
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

seq = 'ACGTACGTAAAAAAAAAAACGTACGT'
hard= 'ACGTACGTNNNNNNNNNNNCGTACGT'
soft= 'ACGTACGTaaaaaaaaaaaCGTACGT'

k = 5 # window size
t = 1.0 # entropy threshold
mask = list(seq)
for i in range(len(seq) -k+1):
	win = seq[i:i+k]
	if entropy(win) > t:
		print(win)
