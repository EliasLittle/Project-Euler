from functions import isPrime, getPermutations


def truncatable(p):
    s = str(p)
    while p > 0:
        if p % 2 == 0:
            return False
        p //= 10

    if any(not isPrime(int(s[i:])) for i in range(0, len(s))):
        return False

    if any(not isPrime(int(s[:i])) for i in range(len(s), 0, -1)):
        return False

    return True


def subString(s):
    n = len(s)
    out = set()
    for Len in range(1, n + 1):
        for i in range(n - Len + 1):
            j = i + Len - 1
            sub = ''
            for k in range(i, j + 1):
                sub += s[k]
            out.add(sub)
    return out


def subPrimes(p):
    out = []
    for i in subString(str(p)):
        if isPrime(int(i)):
            out.append(int(i))
    return out


for i in range(1, 100000, 2):
    if len(subPrimes(i)) > 4:
        if all(isPrime(n[0]) for n in getPermutations(subPrimes(i))):
            print(i)
            print(sum(subPrimes(i)))
            print()
