"""
seq = 'ACGTACGT'

for i in range(len(seq)):
	if seq[i] == 'A': print(seq[i-1]) #print out letter before A

for i, nt in enumerate(seq):
	#print(nt, i)
	if nt == 'A': print(i) 
	
# both methods^ work
#The real code is below
"""

seq = 'ACGTACGTTGCA'

for i in range(len(seq)): #can't skip forward, range goes by ones
	if seq[i] == 'A':
		run_start = i
		run_length = 1
		max_run = 0
		for j in range(i+1, len(seq)):
			if seq[j] == 'A':
				run_length += 1
			else: break
		if run_length > max_run: max_run = run_length
		#print(run_start, run_length) #finds 1st value, runs rest of program itself
		print(max_run)