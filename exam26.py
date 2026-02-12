import sys

def longest_str(strings):
	longest = strings[0] 
	for s in strings[1:]:
		if len(s) > len(longest): longest = s
	return longest, len(longest)

strings = ['hello world', 'pi', 'goku', '3.14159']

print(longest_str(strings))

def tm(s):
	a = s.count('A')
	c = s.count('C')
	g = s.count('G')
	t = s.count('T')
	if lne(s) <= 13: return 2*(a+t) + 4*(c+g)
	else: return 64.9 + 41*(c+g-16.4)/(a+t+c+g)

def highest_tm(oligos):
	tm_max = tm(seq[0])
	save_seq = seq[0]

	for seq in seqs[1:]:
		mytm = tm(seq)
		if mytm > tm_max:
			tm_max = mytm
			save_seq = seq
	
	return tm_max, save_seq

oligos = ['ACGATTTAATCATTT', 'CCAAAAAGGCATTGA', 'AAAAAAAAAAAAAAAA', 'ACG']

print(highest_tm(oligos))
