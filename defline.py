import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline, seq)
	for frame in range(3):
		pro = mcb185.translate(seq[frame:])
		print(pro)