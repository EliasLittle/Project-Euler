def Tn(n): return n*(n+1)/2


def Pn(n): return n*(3*n-1)/2


def Hn(n): return n*(2*n-1)


Tri, Pent, Hex = list(
    map(lambda fn: map(fn, range(10000, 100000)), [Tn, Pn, Hn]))

print(list(set(Tri) & set(Pent) & set(Hex)))
