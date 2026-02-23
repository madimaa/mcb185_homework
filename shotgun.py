import sys
import random

def anti(seq):
	rev = seq[:-1]
	rc = ''
	for nt in rev:
		if   nt == 'A': rc += 'T'
		elif nt == 'C': rc += 'G'
		elif nt == 'G': rc += 'C'
		elif nt == 'T': rc += 'A'


def shotgun_simulation(seq, n, k):
	subs = []
	for _ in range(n):
		x = random.randint(0, len(seq) - k)
		subseq = seq[x:x+k]
		if random.random() < 0.5: subseq = anti(subseq)
		subs.append(subseq)
	return subs
	
	
seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 10 + 26 = 36
print(len(seq))

subseqs = shotgun_simulation(seq, 5, 7) 
print(subseqs)
