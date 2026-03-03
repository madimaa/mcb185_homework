def gc_comp(dna):
	c = dna.count('C')
	g = dna.count('G')
	return c, g, len(dna), (c+g) / len(dna)
dna = input('Enter sequence: ')
print(gc_comp(dna))