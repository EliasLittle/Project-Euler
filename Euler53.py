from math import factorial as fact

def biCoeff(n,k):
	return int(fact(n)/(fact(k)*fact(n-k)))
	
vals = []

for n in range(23,101):
	for k in range(1,n+1):
		v = biCoeff(n,k)
		if v > 1000000:
			vals.append(v)
			
print(len(vals))
