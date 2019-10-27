import functions as f


def g(d, n):
    return d + n/d


tot = 0
for i in range(1, 10000):
    if f.isPrime(i):
        continue
    facts = f.get_factors(i)
    if all(f.isPrime(g(j, i)) for j in facts):
        tot += i

print(tot)
