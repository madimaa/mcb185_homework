import sys

# 2 40 51 - aggie blue
# 255 191 0 - aggie gold

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

min_dis = 1000
min_color = ''
with open(filename) as fp:
	for line in fp:
		colorname, hexvalue, rgbs = line.split() 
		# can either do '\t' or just leave blank ^
		r, g, b = rgbs.split(',')
		distance = 0
		distance += abs(target_r - int(r))
		distance += abs(target_g - int(g))
		distance += abs(target_b - int(b))
		# print(colorname, distance)

		if distance < min_dis:
			min_dis = distance
			min_color = colorname
		

print(min_color, min_dis)