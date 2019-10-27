from math import *

amicable_numbers = set([])

def factor(x):
    divisors = []
    for i in range(1,x):
        if x % i == 0:
            divisors.append(i)
    return(divisors)

def amiCheck(arg):
    if arg == sum(factor(sum(factor(arg)))):
        if arg != sum(factor(arg)):
            amicable_numbers.update([arg, sum(factor(arg))])

def test():
    for i in range(0,7000):
        amiCheck(i)

test()

print(sum(amicable_numbers))
