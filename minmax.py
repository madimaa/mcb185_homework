import sys

dex minmax1(vals):
	mymin = vals[0]
	mymax = vals[0]
	for val in vals[1:]:
		if val < mymin: mymin = val
		if val > mymax: mymax = val
	return mymin, mymax

def minmax2(vals):
	myvals = vals.copy()
	myvals.sort()
	return myvals[0], myvals[-1]

# minmax1 is better, minmax 2 will waste energy copying and creating a whole new list just to do the same thing
