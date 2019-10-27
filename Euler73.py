fractions, tot = {}, 0
for d in range(2, 12001):
    for n in range(d//3-1, d//2+1):
        val = n/d
        if val > 1/3 and val < 1/2 and val not in fractions:
            fractions[val] = True
            tot += 1
print(tot)
