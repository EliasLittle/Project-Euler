sPrime = 10001
pset = [2]
q = 3

def primeCheck(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True

def listxPrimes(given):
    global q
    while(len(pset) < given):
        if primeCheck(q):
            pset.append(q)
        q+=2

listxPrimes(sPrime)
print(pset[sPrime-1])
