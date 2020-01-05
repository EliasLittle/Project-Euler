import math
from timeit import default_timer as timer

# Returns GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Returns Eulers Totient function, the number relatively prime numbers
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

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
def get_factors(n, primelist=None,count=False):
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

    if count==True:
        return sum([f[0] for f in fcount])

    factors = [1]
    for i in fcount:
        level = []
        exp = [i**(x+1) for x in range(fcount[i])]
        for j in exp:
            level.extend([j*x for x in factors])
        factors.extend(level)

    return factors

#number of prime factors
def number_prime_factors(number):
    i = 2
    a = set()
    while i < math.sqrt(number) or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

# get a list of prime factors
# ex: get_prime_factors(140) -> ((2,2), (5,1), (7,1))
#     140 = 2^2 * 5^1 * 7^1
def get_prime_factors(n, plist=None):
    if plist is None:
        primelist = prime_sieve(n, output=[])
    else:
        primelist = plist

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
def isPandigital(num, max=9,zero=False):
    l = max+1 if zero else max
    s = len(str(num))
    if s != l:
        #raise Exception("Length must be {}, but was {}".format(l,s))
        return False
    for i in range(0 if zero else 1, max+1):
        if str(i) not in str(num):
            return False
    return True


#Returns a list of the possible permutations
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

#Same as getPermutations, but yields them as they are found
#Accepts array of values
def yieldPermutations(A):
    n = len(A)
    B = A
    yield tuple(A)
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
            yield tuple(temp)
        else:
            c[i] = 0
            i += 1

# Recursive factorial funcion
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

# Checks if n is palindromic
def isPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

"""
HELPER FUNCTIONS
"""

# Concatenates all integers of a list to a single integer
# Inverse of digits
def toInt(A):
    sum = 0
    dlens = [int(math.log10(d))+1 if d > 0 else 1for d in A] # Length of each digit
    c = 0
    for i in range(len(A),0,-1):
        sum += A[i-1]*math.pow(10,c)
        #print("sum: "+str(sum))
        c+=dlens[i-1]
        #print("c: "+str(c))
    return int(sum)

# Returns a list of the digits of int n
# Inverse of toInt
def digits(n):
    len = int(math.log10(n))+1
    return [int((n//math.pow(10,len-i-1))) % 10 for i in range(len)]


if __name__ == '__main__':
    print(toInt([1,2,3]))
