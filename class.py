import math
def mean(values):
	total = 0
	for value in values:
		total = total + value
	return total / len(values)

def entropy(P):
	if not math.isclose(mysum(P), 1.0): sys.exit('nooooo')
	H = 0
	for p in P: 
		H -= p * math.log2(p)
	return H

x = [0.1, -3, 39, 4.5]
print(mean(x))
print(entropy(x))
