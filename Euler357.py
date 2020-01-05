from functions import *

def g(d, n):
    return d + n/d

tot = 0
primes = prime_sieve(1000000,output=[])
print("Prime list of 1,000,000 found")
for i in range(1, 10000):
    if i%1000== 0:
        print(""+str(i/1000)+"% done")
    if i in primes:
        tot += i
        continue
    facts = get_factors(i,primelist=primes)
    add = True
    for j in facts:
        if g(j,i) not in primes:
            add = False
            break
    if add:
        tot += i

print(tot)
