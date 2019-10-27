def f(a, n):
    m = pow(a, 2)
    return (pow(a-1, n, m) + pow(a+1, n, m)) % m


def max(a):
    max = 0
    for i in range(1, f(a, 1), 2):
        val = f(a, i)
        if val > max:
            max = val
    return max


tot = 0

for a in range(3, 1001):
    tot += max(a)

print(tot)
