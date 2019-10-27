from functions import isPrime, prime_sieve


def truncatable(p):
    s = str(p)
    while p > 0:
        if p > 2 and p % 2 == 0:
            return False
        p //= 10

    if any(not isPrime(int(s[i:])) for i in range(0, len(s))):
        return False

    if any(not isPrime(int(s[:i])) for i in range(len(s), 0, -1)):
        return False

    return True


out = []
primes = prime_sieve(1000000)
for i in primes:
    if i < 10:
        continue
    if truncatable(i):
        out.append(i)
print(sum(out))
