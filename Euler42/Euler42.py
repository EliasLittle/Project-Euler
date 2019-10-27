file = open(r'/Users/EliasL/Documents/Code/Project Euler/Euler42/p042_words.txt')
words = file.read().split(',')

for i in range(len(words)):
    words[i] = words[i][1:-1]


def tri(n):
    return int(0.5 * n * (n+1))


triNums = [False for i in range(1000)]
n = 1
while True:
    if tri(n) >= 1000:
        break
    triNums[tri(n)] = True
    n += 1


def isTri(str):
    sum = 0
    for char in str:
        sum += (ord(char) - 64)
    return triNums[sum]


tot = 0
for i in words:
    if isTri(i):
        tot += 1

print(tot)
