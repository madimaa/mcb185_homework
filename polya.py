seq = 'ACGTACGTTGCAACTGGCTAAAAAAA'
max_run = 0
i = 1
while i < len(seq):
	if seq[i] == 'A':
		run_start = i
		run_length = 1
		for j in range(i+1, len(seq)):
			if seq[j] == 'A':
				run_length += 1
			else: break
		i = j
		if run_length > max_run: max_run = run_length
	i += 1
print(max_run)
