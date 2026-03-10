# dust, entropy filter
import argparse
import math
def entropy(s):
	pa = s.count('A') / len(s)
	pc = s.count('C') / len(s)
	pg = s.count('G') / len(s)
	pt = s.count('T') / len(s)
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc) #can't do this if there are no c's in window
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h

def dust(seq, k, t):
	sed = list(seq)
	for i in range(len(seq) -k+1):
		if entropy(seq[i:i+k]) < t:
			for j in range(i, i+k):
				sed[j] = 'N'
	return ''.join(sed)

#could be on exam^: need to write both entropy and dust

#parse stuff is optional
#parser = argparse.ArgumentParser()
#parser.add_argument('seq')
#parser.add_argument('k', type=int, default=7)
#parser.add_argument('--threshold', type=float, default=1.0, help='%(default)f.3')
#parser.add_argument('--soft', action='store_true')
#arg = parser.parse_args()

seq = 'ACGTAAAAAAAAACGTACGT'
sed = list(seq)

# mask = hide the low complexity (multiple A's) with N
k = 7 # window size
t = 1.0 # entropy threshold
soft = False
for i in range(len(seq) -k+1):
	win = seq[i:i+k]
	if entropy(win) < 1.0:
		for j in range(i, i+k):
			if soft: sed[j] = sed[j].lower() #soft
			else: sed[j] = 'N' #hard
print(''.join(sed))