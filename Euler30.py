vals = []

i = 2
while len(vals) < 6:
    if i == sum([pow(int(d), 5) for d in str(i)]):
        vals.append(i)
    i += 1

print(vals)
