a = 3
b = 4
c = (a**2 + b**2)**0.5
print('hello world', a, b, a + b, a**2, b**2)
print(type(a), type(b),type(c))
print('pythagoras', a, b, c)

def is_prime(n):
        for i in range(3, n):
                print('checking', i)
                r = n % i
                if r == 0: return False
        return True 

for i in range(1,101):
        if i % 15 == 0:
                print('fizzbuzz')
        elif i % 3 == 0:
                print('fizz')
        elif i % 5 == 0:
                print('buzz')
        else:
                 print(i, end='')

