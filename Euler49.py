from functions import prime_sieve, yieldPermutations, digits, toInt

primes = prime_sieve(10000)

# If one exists, it returns the three elements of a sorted array that form an arithmetic sequence
def seq(A):
    d=[[(A[i]-A[0],0)] for i in range(1,len(A))]
    for i in range(1,len(A)):
        for j in range(i+1,len(A)):
            v2 = A[j]-A[i]
            for k in d[i-1]:
                if v2==k[0]:
                    return [A[k[1]],A[i],A[j]]
            d[j-1].append((v2,i))
    return False

candidates = set()

for p in primes:
    if p < 1000:
        continue
    pps = set()
    for i in yieldPermutations(digits(p)):
        n = toInt(i)
        if n < 1000:
            continue
        if n in primes:
            pps.add(n)
    if len(pps) >= 3:
            candidates.add(tuple(sorted(list(pps))))

for i in candidates:
    t = seq(list(i))
    if t != False:
        print(t)
        print(toInt(t))

print("length: "+str(len(candidates)))
