
s = 'hello this is fun!'
characters = []
char_count = []
for c in s:
	if c not in characters:
		#print('first time seeing', c)
		characters.append(c)
		char_count.append(1)
	else: 
		#print('seen this', c, 'before, adding 1')
		idx = characters.index(c)
		char_count[idx] += 1

#for c, n in zip(characters, char_count):
	#if ord(c) <= 32: print(ord(c), n)
	#print(c, n)
	
for i in range(len(characters)):
	print(characters[i], char_count[i])
	
	

#chars = [0] * 128
#for c in s:
	#chars[ord(c)] += 1
#for i in range(len(chars)):
	#if chars[i] == 0: continue #skip
	#print(ascii(i), chars[i])