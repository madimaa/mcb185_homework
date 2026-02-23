import sys
import random

genome_size = int(sys.argv[1])
coverage = int(sys.argv[2])

genome = [0] * genome_size

for i in range(genome_size * coverage):
	pos = random.randint(0, genome_size-1)
	genome[pos] += 1

zeroes = 0
for v in genome:
	if v < 8: zeroes += 1
	
print(1-zeroes/genome_size)