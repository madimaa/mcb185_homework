import math
import argparse
import mcb185

#entropy func
def entropy(seq):
	pa = seq.count('A') / len(seq)
	pc = seq.count('C') / len(seq)
	pg = seq.count('G') / len(seq)
	pt = seq.count('T') / len(seq)
	h = 0
	if pa != 0: h -= pa * math.log2(pa)
	if pc != 0: h -= pc * math.log2(pc)
	if pg != 0: h -= pg * math.log2(pg)
	if pt != 0: h -= pt * math.log2(pt)
	return h

#argparse stuff is optional and just if you want to be professional
parser = argparse.Argumentparser()
parser.add_argument('fasta')
parser.add_argument('--k', type=int, default=11)
parser.add_argument('--threshold', type=float, default=1.1)
parser.add_argument('--hard', help='perform hard')
arg = parser.parse_args()

seq = 'ACGTACGTAAAAAAAAAAACGTACGT'
hard= 'ACGTACGTNNNNNNNNNNNCGTACGT'
soft= 'ACGTACGTaaaaaaaaaaaCGTACGT'

k = arg.window
t = arg.threshold
for defline, seq in mcb185.read_fasta(arg,fasta):
#k = 5 # window size
#t = 1.0 # entropy threshold
	mask = list(seq)
	for i in range(len(seq) -k+1):
		if entropy(seq[i:i+k]) > t: continue
		for j in range(i, i+k):
			mask[j] = 'N' # hard
			#mask[j] = seq[j].lower() # soft
	print(''.join(mask))

