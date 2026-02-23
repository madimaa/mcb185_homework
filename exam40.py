import random
import sys

def mutate(s, p):
	seq = list(s)
	for i in range(len(seq)):
		if random.random() < p:
			if seq[i] == 'A': seq[i] = random.choice('CGT')
			elif seq[i] == 'C': seq[i] = random.choice('AGT')
			elif seq[i] == 'G': seq[i] = random.choice('ACT')
			elif seq[i] == 'T': seq[i] = random.choice('ACG')
	return ''.join(seq)

dna = 'AAAAAAAAAAAAAAAAAAAAAAAA'
dna = mutate(dna, 0.9)

print(dna)