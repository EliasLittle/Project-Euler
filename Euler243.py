from functions import phi, prime_sieve


check = 15499/94744
"""
for i in range(2,94744):
    if i%1000 == 0:
        print i/1000, "%"
    if 1.0*phi(i)/(i-1) < check:
        print(i)
        break
"""
primes=prime_sieve(50000,output=[])

val = 1
for p in range(2,50000):
    if val>1000000:
        print "Exceeded limit"
        break
    #print(val)
    val*=p
    if 1.0*phi(val)/(val-1) < 0.4:
        print(val)
        break
