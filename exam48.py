#python3 gc_analysis ATATACAAATTACGAT 7
#2 parts, seq and window size
import sys
seq = sys.argv[1]
k = int(sys.argv[2]) #remember to int() window size
"""
first = seq[0:k]
g = first.count('G')
c = first.count('C')
for i in range(len(seq) - k+1):
	off seq[i]
	on seq[i+k]
	if off =='C': c -= 1 
	elif off =='G': g -= 1
	if on =='C': c += 1 
	elif on == 'G': g += 1
print(i, win)
"""
#The professional way fo doing it^
#The below v is good for exam
for i in range(len(seq) - k+1):
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	gc_comp = (c+g) / k
	#gc_skew = (g-c) / (g+c) if g+c != 0 else 0 #can do this too for same result
	if g+c == 0: gc_skew = 0 #This is for when the window has no g's nor c's
	else:        gc_skew = (g-c) / (g+c)
	print(i, win, c, g, (c+g) / k)
	
