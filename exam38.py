import random
import math

def random_dna(n, X = [0.25, 0.25, 0.25, 0.25]):
	total = sum(X)
	a = X[0]/total
	c = X[0] + X[1]/total
	g = X[[0] + X[1] + X[2] / total
	rseq = ''
	for _ in range(n):
		r = random.random()
		if   r < a: rseq += 'A'
		elif r < c: rseq += 'C'
		elif r < g: rseq += 'G'
		else:       rseq += 'T'
	return rseq

for i in range(5):
	print(i, random_dna(10))
