seq = 'GATCACGAT'
seq_list = list(seq)
seq_list[3] = 'a'
seq_list.sort()
s = '-'.join(seq_list)

print(seq)
print(seq_list)
print(s)
