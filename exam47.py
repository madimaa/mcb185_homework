import sys
def read_fasta(filename):
	#get file open, glue stuff onto empty var
	filename = sys.argv[1]
	seq = []
	with open(filename) as fp:
		for line in fp:
			seq.append(line.rstrip()) #rstrip strips off any char on right hand side of line
	seqline = ''.join(seq[1:])
	words = seq[0]
	uid = words.split()[0][1:] #1st word then 1st character onward
	return uid, len(seqline)
	
uid, seq = read_fasta(sys.argv[1])
print(uid, seq)