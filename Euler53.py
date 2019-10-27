from math import factorial as f


def nCr(n, r):
    return f(n)/(f(r)*f(n-r))


out = 0
for n in range(1, 101):
    for r in range(1, n):
        if nCr(n, r) > 1000000:
            out += n-r+1
            break
    else:
        continue

print(out)
