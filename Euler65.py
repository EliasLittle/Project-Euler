#SOLVED

#Helper function for testing
def fracPrint(ab):
    print(""+str(ab[0])+"/"+str(ab[1]))
approx = [(2,1),(3,1)]

#solves for the next numerator and denominator of the next convergent of the continued fraction for e
#uses the two previous fractions
def next(A,n):
    f = 2*(n//3+1) if (n+2)%3==0 else 1
    num = f*A[n][0]+A[n-1][0]
    den = f*A[n][1]+A[n-1][1]
    approx.append((num,den))

for i in range(1,99):
    next(approx,i)

a=approx[len(approx)-1]
n=a[0]
d=a[1]
print(n*1.0/d)
print(sum(int(digit) for digit in str(a[0])))
