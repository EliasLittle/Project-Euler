from math import *

def sieve(n):
    primes = [True for i in range(n+1)]
    x=2
    while (x*x <= n):
        if (primes[x] == True):
            for i in xrange(x*x, n+1, x):
                primes[i] = False
        x+=1

    return primes

sieveSet = sieve(1000000)
primeSet = []
for i in xrange(2, len(sieveSet)):
    if sieveSet[i]:
        primeSet.append(i)

def circular(n):
    num = str(n)
    if any(c in num for c in'024568'):
        return False
    for i in xrange(len(num)):
        if int(num) not in primeSet:
            return False
        num = num[-1]+num[0:-1]
    return True


circularSet = [2,5]
for i in primeSet:
    if circular(i):
        circularSet.append(i)

print(len(circularSet))
