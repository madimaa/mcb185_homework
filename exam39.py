import sys
import random

# seq = string
# n = vals returned
# k = length of val returned
def random_subseq(seq, n, k):
	subs = []
	for _ in range(n):
		x = random.randint(0, len(seq) - k)
		subseq = seq[x:x+k]
		subs.append(subseq)
	return subs
	
	
seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 10 + 26 = 36
print(len(seq))

subseqs = random_subseq(seq, 5, 7) 
print(subseqs)