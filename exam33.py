import math
import sys

def dkl(P, Q):
	if not math.isclose(1.0, sum(P)): sys.exit('error')
	if not math.isclose(1.0, sum(Q)): sys.exit('error')
# make sure the histograms ^ sum to 1, that's why we math.isclose here
	distance = 0
	for p, q in zip(P, Q):
		if p == 0: continue
		if q == 0: continue
		distance = p * math.log2(p/q)
	return -distance
	
a = [0.25, 0.25, 0.25, 0.25]
b = [0.4, 0.3, 0.2, 0.1]

print(dkl(a, b))