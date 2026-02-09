s = 'ACGTAGATCGAG'
if 'A' in s: print('yes, found A')
if 'AGT' in s: priont('yes, found ACG')
x = s.index('A')
print('A found at pos', x)
y = s.find('Y')
print('Y found at pos', y)

animals = ['cat', 'dog', 'cow', 'pig']
if 'cow' in animals:
	x = animals.index('cow')
	print(x)
