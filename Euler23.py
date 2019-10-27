import math


def factor(x):
    divisors = {1}
    largest = int(math.sqrt(x))
    if largest * largest != x:
        largest += 1
    else:
        divisors.add(largest)
    for i in range(2, largest):
        if x % i == 0:
            divisors.add(i)
            divisors.add(x/i)
    return(divisors)


def abundant(n):
    if sum(factor(n)) > n:
        return True
    return False


rng = {x: abundant(x) for x in list(range(1, 28126))}
abdntNums = [item for item in rng if rng[item] == True]
print("Abundant numbers: ")
print(abdntNums)


def abundantSum(num):
    i = 0
    while abdntNums[i] < num//2+1:
        if rng[num - abdntNums[i]] == True:
            return True
        i += 1
    return False


nonAbSumNums = [i for i in range(1, 28125) if abundantSum(i) == False]
print("Non abundant sum numbers: ")
print(nonAbSumNums)

sum = 0
for val in nonAbSumNums:
    sum += val
print(sum)
