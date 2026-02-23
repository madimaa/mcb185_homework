import sys

vals = []
for s in sys.argv[1:]:
	vals.append(float(s))
	
# number of values
print(len(vals))

# maximum and minimum
vals.sort()
print('min: ', vals[1])
print('max: ', vals[-1])	

# get the total
total = 0
for val in vals: 
	total += val
# calculate mean
mean = total/len(vals)
# calculate standard dev
total = 0
for val in vals:
	total += (val - mean)**2
sd = (total / len(vals))**0.5

print('mean: ', mean)
print('Standard Deviation: ', sd)

#median
m = len(vals) // 2 # m is higher index, m-1 is lower index
if len(vals) % 2 == 1:
	print('it\'s odd') 
	median = vals[m]
else: median = (vals[m] + vals[m-1]) / 2
print('median: ', median)