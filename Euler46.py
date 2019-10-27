from functions import isPrime
from math import sqrt


def test(n):
    for j in range(1, int(sqrt(n/2))+1):
        val = n - 2*pow(j, 2)
        if isPrime(val):
            return True
    return False


run = True
i = 9
while run:
    if isPrime(i):
        i += 2
        continue
    if not test(i):
        print("Answer: " + str(i))
        run = False
        break
    i += 2
