import sys
import random

num_days = int(sys.argv[1])
num_ppl = int(sys.argv[2])

#cal = list()
#for _ in range(num_days):
#	cal.append(0)
#another way of turning calendar into a list^

cal = [0] * num_days
#Fill cal with dates and check as you go
found = False
for i in range(num_ppl):
	date = random.randint(0, num_days-1)
	cal[date] += 1
	if cal[date] > 1:
		found = True
		break
print(cal, found)



#2 types of for loops: for _ in range() and for item in container
#Only use i, j, k for range()