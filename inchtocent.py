def inch_to_cm(x):
	 return x * 2.54

for inch in range(20):
	cm = inch_to_cm(inch)
	print(inch, cm)

print(inch_to_cm(1))
print(inch_to_cm(10))
