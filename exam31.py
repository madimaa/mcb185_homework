import math
import sys

def percent_id(s1, s2):
	diff = 0
	for c1, c2 in zip(s1, s2):
		if c1 != c2: 
			diff += ((c1 - c2)**2)**0.5
	length = len(s1)
	return (diff/length)*100
a = [0.4, 0.3, 0.2, 0.1]
b = [0.4, 0.6, 0.0, 0.0]

s1 = 'ACGTACGT'
s2 = 'TGCATGCA'

print(percent_id(a, b))
#print(percent_id(s1, s2))