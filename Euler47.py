import functions
import numpy as np
from functions import get_prime_factors as gpf
import array
#from bitarray import bitarray

'''
count = 0
nums = []
n = 4
digits = 4

#print(len(gpf(14)))
#print(len(gpf(15)))

while len(nums) < digits and n < 1000000:
    if len(gpf(n)) == digits:
        #print(n)
        nums.append(n)
        if len(nums) > digits-1:
            print("Length:", len(nums), n)
            break
        n+=1
    else:
        del nums[:]
        n += 14-(n%10)


print(nums)
'''
base_primes = [2]
primes = set(functions.prime_sieve(10, []))-set(base_primes)

def sieve(prime_factors):
    flags = [True for i in range(1,1001)]
    for i in prime_factors:
        l = len(flags)//i
        #print(l)
        flags[i::i] = [False]*(l+l%2-1) #Sets all multiples to false
    return list(flags)

for p in primes:
    p_factors = base_primes + [p]
    rel_pr = sieve(p_factors)
    print(rel_pr)
    for i in range(len(rel_pr)-2):
        if rel_pr[i] and rel_pr[i+1]:
            print(i)
