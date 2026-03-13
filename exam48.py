seq = 'ACGTACGTAAAAAA'
k = 4
"""
For seq and k, these could come from the command line, 
which you would need to import sys for
"""
for i in range(0, len(seq) -k+1):
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	gc_comp = (g+c) / k
	if (g+c) == 0: gc_skew = 0
	else: gc_skew = (g-c) / (g+c)
	print(i, gc_comp, gc_skew)