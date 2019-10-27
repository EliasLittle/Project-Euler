combos = []

for a in range(2, 101):
    for b in range(2, 101):
        val = a**b
        if val not in combos:
            combos.append(val)

print(len(combos))
