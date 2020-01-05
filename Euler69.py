from functions import phi, prime_sieve

x=1
primes = prime_sieve(10000,[])
i = 0
while x*primes[i] <=1000000:
    x=x*primes[i]
    i+=1
print(x)
