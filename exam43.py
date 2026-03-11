import sys
import random

cal = int(sys.argv[1])
num = int(sys.argv[2]) #number of people #DONT FORGET TO int()

shared_birthdays = 0
rounds = 50
for g in range(rounds):
	shared = False
	birthdays = list()
	for _ in range(num): #use _ for integers, NOT for strings
		birthdays.append(random.randint(0, cal-1))
	for i in range(num):
		for j in range(i+1, num):
			if birthdays[i] == birthdays[j]:
				shared = True #the shared thing = will never print 'hooray' >1 time
	if shared: shared_birthdays += 1
print(shared_birthdays)