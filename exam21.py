seq = input('Enter sequence:')
c = seq.count('C')
g = seq.count('G')

print(c, g, len(seq), (c+g) / len(seq))
