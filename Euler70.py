import math
import collections
from functions import get_prime_factors

def phi(n):
    totient = n
    for factor in get_prime_factors(n):
        totient -= (totient // factor)
    return totient

vals = []

def digits(n):
    return [int(d) for d in str(n)]

def compare(x,y):
    return collections.Counter(digits(x)) == collections.Counter(digits(y))

def test(n):
    p = phi(n)
    if len(str(p)) != len(str(n)):
        return False
    elif compare(n,p):
        vals.append([n,p])
        return True

for n in range(1, int(math.pow(10, 5)), 6):
    test(n)



#print(test(87109))
print(vals)
