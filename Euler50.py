from math import *

primeSet=[]
def makePrimeSet(maxRange):
    for i in range(2,maxRange):
        if isPrime(i):
            primeSet.append(i)

def isPrime(n):
    if n < 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int( sqrt(n) )+1):
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True

numPrimes = 1000
makePrimeSet(numPrimes)
print "Primes under", numPrimes, "is", len(primeSet)

sum = 0
count = 0
for i in primeSet:
    if (sum+i) < 1000:
        sum+=i
        count+=1

#print "Count:", count
print "Largest Sum:", sum
print "Largest Count:", count

while not isPrime(sum):

        sum = sum - primeSet[count-1]
        #print "Updated Sum:", sum
        count-=1

print "Final Sum:", sum
