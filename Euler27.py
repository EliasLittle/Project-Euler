from math import *

def f(a,b,n):
    return n*n+a*n+b

def test(a,b):
    n=0
    while isPrime(f(a,b,n)):
        n+=1
    return n

def isPrime(n):
    if n < 0:
        n=-n
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

longPair = [0,0]
longest = 0

bprimes=[]
for i in range(1000):
    if isPrime(i):
        bprimes.append(i)

for a in range(-997,997,6):
    for b in bprimes:
        m = test(a,b)
        if m > longest:
            longest  = m
            longPair = [a,b]

#TODO: Create alternate that returns the most unique primes

aVal=longPair[0]
bVal=longPair[1]
print("a: "+str(aVal)+" & b: "+str(bVal))
print("Longest string: "+str(longest))
print("Product: "+str(aVal*bVal))
print(" ")
