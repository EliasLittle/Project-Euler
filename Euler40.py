s = ''.join([str(i) for i in range(190000)])
print(s[:40])

val = 1
i = 1
while i <= 1000000:
    val *= int(s[i])
    i *= 10

print(val)
