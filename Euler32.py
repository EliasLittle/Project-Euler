from functions import isPandigital

needed = set(str(i) for i in range(1, 10))
out = set()
for i in range(5000, 0, -1):
    remaining = needed-set(str(i))
    for j in range(i, 0, -1):
        v = i*j
        if v > 9999:
            continue
        if any(i in remaining for i in str(i)):
            continue
        if any(n in str(j)+str(i) for n in str(v)):
            continue
        if isPandigital(int(str(i)+str(j)+str(v))):
            out.add((v))

print(sum([o for o in out]))
