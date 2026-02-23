import sys

vals = []
for s in sys.argv[1:]:
	vals.append(float(s))

vals.sort()
total = 0
for val in vals: total += val
mean = total / len(vals)

# 1 3 7 19 15 20 (6 long // 2 = 3)

#median
m = len(vals) // 2 # m is higher index, m-1 is lower index
if len(vals) % 2 == 1:
	print('it\'s odd') 
	median = vals[m]
else: median = (vals[m] + vals[m-1]) / 2


print('minimum: ', vals[0])
print('maximum: ', vals[-1])
print('range: ', vals[-1] - vals[0])
print('average: ', mean)
print('median: ', median)