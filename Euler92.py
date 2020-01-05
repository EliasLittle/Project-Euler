# SOLVED (but extremely slow)
import math

count = {89: 1, 1: 1}

found = {89:89,1:1}

def chain(n):
    digits = [n//math.pow(10,i)%10 for i in range(int(math.log10(n))+1)]
    return int(sum(math.pow(d,2) for d in digits))

for i in range(1,1000000):
    n = i
    stack = []
    while n not in found:
        #print(n)
        k = chain(n)
        if k in found:
            stack.append(n)
            for j in stack:
                found[j] = found[k]
                count[found[k]] = count[found[k]]+1
            #print(found)
        else:
            stack.append(n)
        n = k


print(count)
#print(found)
