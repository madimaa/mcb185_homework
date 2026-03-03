import random

def random_word_list(n, k): #n words, k letters long
	words = set() 
	for _ in range(n):
		word = ''
		for j in range(k):
			letter = random.choice('ABCDEFGHIJ')
			word += letter
		words.add(word)
	return words
	
size = 10_000 #underscore doesnt do anything here, number still 10,000
words1 = random_word_list(size, 5) 
words2 = random_word_list(size, 5)
#adding a 0 to size will increase time by 100x

found = 0
for word in words1:
	if word in words2:
		print('hooray, found', word)
		found += 1
print('found', found)

#making random_word_list(n, k) a set instead of a list decreases time to complete exponentially
#Set is like list but not ordered