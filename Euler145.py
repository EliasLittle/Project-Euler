def reverse(n):
    return int(str(n)[::-1])


def reversible(val):
    while val:
        if val % 2 == 0:
            return False
        val //= 10
    return True


reversibles = 0
reverses = 0
count = 0

for i in range(1, 10000000, 2):
    r = reverse(i)
    reverses += 1
    if r % 2 != 0:
        continue
    reversibles += 1
    if reversible(i+r):
        count += 2

print("Count: " + str(count))
print("Reverses: " + str(reverses))
print("Reversibles: " + str(reversibles))
