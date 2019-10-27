from functions import factorial

out = []
for i in range(3, 1000000):
    if i == sum([factorial(int(j)) for j in str(i)]):
        out.append(i)

print(out)
print(sum(out))
