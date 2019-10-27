coins = [1,2,5,10,20,50,100,200]
target  = 200

ways = [0 for i in range(target+1)]
ways[0] = 1

for i in coins:
    for j in range(i,target+1):
        ways[j] += ways[j - i]

print(ways)
