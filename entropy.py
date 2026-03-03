import math
def entropy(seq):
	h = 0
	pa = seq.count('A') / len(seq)
	pc = seq.count('C') / len(seq)
	pg = seq.count('G') / len(seq)
	pt = seq.count('T') / len(seq)
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h
	
seq = 'ACGTACGTACGTACGTAAAAAAACCCCCCCCGGGGGGGGGGTTTTTTT'
# bunch of the same letters in a row = low entropy = masked by 'N'
w = 5
t = 1.5
mask = list(seq)
for i in range(len(seq) -w+1):
	win = seq[i:i+w]
	h = entropy(win)
	if h < t:
		for j in range(i, i+w):
			mask[j] = 'N'
print(''.join(mask))