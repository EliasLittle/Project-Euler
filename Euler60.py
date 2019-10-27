# UNSOLVED

import functions as f

primes = f.prime_sieve(10000, [])
pblts = []

for prime in primes:
    subs = [prime]
    for i in range(0, primes.index(prime)):
        if str(primes[i]) in str(prime):
            subs.append(primes[i])
    if len(subs) >= 3:
        pblts.append(subs)


count = {i: 0 for i in primes}
for set in pblts:
    for i in range(1, len(set)):
        count[set[i]] += 1

for i in count.keys():
    if count[i] >= 4:
        print(i, count[i])
