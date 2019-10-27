#UNSOLVED.... :(


import time

#csum_time = 0
#test_time = 0


def csum(val):
    #global csum_time
    #start = time.time()
    tot = 0
    while val:
        tot += val % 10
        val //= 10
    #end = time.time()
    #csum_time += (end-start)
    return tot


def test(val):
    #global test_time
    tot = csum(val)
    #start = time.time()
    if tot == 1 or tot == 0:
        return False
    if val % tot != 0:
        return False
    if val//tot % tot != 0:
        return False
    n = tot
    i = 1
    while n <= val:
        if n == val:
            print(i)
            #end = time.time()
            #test_time += (end-start)
            return True
        i += 1
        n *= tot
    #end = time.time()
    #test_time += (end-start)
    return False


def altest(val):
    tot = csum(val)
    if tot == 1 or tot == 0:
        return False
    if val % tot != 0:
        return False
    while val/tot == val//tot:
        if val == 0:
            return True
        val /= tot
    return False


series = []

i = 11
while len(series) != 10:
    if test(i):
        series.append(i)
    i += 1

print(series)

'''
runs = 10000000

print("Test")
#start = time.time()
for i in range(runs):
    test(i)
#end = time.time()
#print("Time: "+str((end-start)/runs))

print(csum_time / runs)
print(test_time / runs)
'''
