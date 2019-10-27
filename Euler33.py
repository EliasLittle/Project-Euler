# For fractions a/b
import math


def cancDigits(a, b):
    for i in range(2):
        for j in range(2):
            a_s = str(a)
            b_s = str(b)
            if a_s[i] == b_s[j]:
                return map(int, [a_s[1-i], b_s[1-j], a_s[i], b_s[j]])
    return [0, 0, 0, 0]


pairs = []

for b in range(11, 100):
    for a in range(10, b):
        arr = list(cancDigits(a, b))
        vals, aVal = arr[:2], arr[2:]
        if aVal[0] == 0 or aVal[1] == 0:
            continue
        if vals[0] != 0 and vals[1] != 0:
            if float(a/b) == float(vals[0]/vals[1]):
                # print("a: ", a, " b: ", b)
                # print(float(a/b))
                # print(float(vals[0]/vals[1]))
                pairs.append([a, b])

num, den = 1, 1
for pair in pairs:
    num *= pair[0]
    den *= pair[1]

cf = 1
for i in range(int(num), 1, -1):
    if num % i == 0 and den % i == 0:
        cf = i
        break
num, den = num/cf, den/cf

print("Simplified Denominator: ", den)
