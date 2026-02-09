a = ['cat', 'dog', 'rat']
b = a.copy()

for animal in a:
	b.append(animal)

b[0] = 'cow'

print(a)
print(b)
