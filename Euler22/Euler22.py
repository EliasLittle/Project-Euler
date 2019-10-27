import string

names = open(r'/Users/EliasL/Documents/Code/Project Euler/Euler22/Euler22.txt')
nameArr = names.read().split(',')
nameArr.sort()
for i in range(len(nameArr)):
    nameArr[i] = nameArr[i][1:-1]
scores = []

for name in nameArr:
    rawScore = 0
    for char in name:
        rawScore += ord(char)-64
    scores.append(rawScore)

sum = 0
for i in range(len(scores)):
    sum+=scores[i]*(i+1)

print sum
