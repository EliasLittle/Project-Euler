import math

# Returns GCD


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Checks if a number is prime O(sqrt(n))


def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


# return a dict or a list of primes up to N
# create full prime sieve for N=10^6 in 1 sec
def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * int((m+1))

    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    elif type(output) == list:
        return [x for x in sieve if x != 0]
    else:
        return None


def prime_generator(n):
    for i in range(n, 2, -1):
        if isPrime(i):
            yield i


# get a list of all factors for N
# ex: get_factors(10) -> [1,2,5,10]
def get_factors(n, primelist=None):
    if primelist is None:
        primelist = prime_sieve(n, output=[])

    fcount = {}
    for p in primelist:
        if p > n:
            break
        if n % p == 0:
            fcount[p] = 0

        while n % p == 0:
            n /= p
            fcount[p] += 1

    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            level.extend([j*x for x in factors])
        factors.extend(level)

    return factors


# get a list of prime factors
# ex: get_prime_factors(140) -> ((2,2), (5,1), (7,1))
#     140 = 2^2 * 5^1 * 7^1
def get_prime_factors(n):
    # if primelist is None:
    primelist = prime_sieve(n, output=[])

    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs.append((p, count))

    factors = []
    for pair in fs:
        # for i in range(0,pair[1]):
        factors.append(pair)
    return factors


# returns whether num is a 9 digit isPandigital
def isPandigital(num, max=9):
    if len(str(num)) != max:
        return False
    for i in range(1, max+1):
        if str(i) not in str(num):
            return False
    return True


def getPermutations(A):
    n = len(A)
    out, B = [], A
    out.append(tuple(A))
    c = [0 for i in range(n)]

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                B[0], B[i] = B[i], B[0]
            else:
                B[c[i]], B[i] = B[i], B[c[i]]
            c[i] += 1
            i = 0
            temp = B
            out.append(tuple(temp))
        else:
            c[i] = 0
            i += 1
    return out

"""
Needs to be finished, currently just outlined
def recursivePermutations(A):
    s = set([c for c in A])
    return ([n + recursivePermutations(s.remove(n)) for n in s])
"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

def isPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    pass
