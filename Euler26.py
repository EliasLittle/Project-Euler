# SOLVED, but most inellegant solution ever...
import decimal as d


def lam(n):
    if len(str(1/n)) < 18:
        return (0, 0)
    d.getcontext().prec = 100000
    s = str(d.Decimal(1)/d.Decimal(n))[2:]
    # print(s)
    delta = 100

    def t_loc(t): return s[t:t+delta]

    def h_loc(h): return s[h:h+delta]

    t = 0
    h = 2
    while t_loc(t) != h_loc(h):
        t += 1
        h += 2

    mu = 0
    t = 0
    while t_loc(t) != h_loc(h):
        t += 1
        h += 2
        mu += 1

    lam = 1
    h = t+1
    while t_loc(t) != h_loc(h):
        h += 1
        lam += 1
    return lam, mu


max_n = 0
max_l = 0
for n in range(1, 1001):
    cycle_length = lam(n)[0]
    # print(f"Testing {n}")
    # if cycle_length > 100:
    # print(str(d.Decimal(1)/d.Decimal(n))[2:])
    # print(f"Length is {cycle_length}")
    # print(" ")
    if cycle_length >= max_l:
        max_n = n
        max_l = cycle_length

print(f"Answer: {max_n}")
print(f"With length {max_l}")
