fractions, tot = set(), 0
for d in range(2, 1000000):
    for n in range(d):
        val = n/d
        if val not in fractions:
            fractions.add(val)
            tot += 1
print(tot)
