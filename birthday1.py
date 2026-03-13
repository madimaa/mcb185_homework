import sys
import random
#point = get all birthdays into a list
num_days = int(sys.argv[1])
num_ppl = int(sys.argv[2])
#check everyone against everyone else
birthdays = list()
found = False
for i in range(num_ppl):
	date = random.randint(0, num_days-1)
	birthdays.append(date)
for i in range(0, num_ppl):
	for j in range(i+1, num_ppl):
		if birthdays[i] == birthdays[j]:
			found = True
	if found: break
print(birthdays, found)