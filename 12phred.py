def char_to_prob(x):
	return ord(x)/100
def prob_to_char(y):
	return chr(y)*100
print(char_to_prob('A'))
print(prob_to_char(0.001))
print(char_to_prob('!'))
