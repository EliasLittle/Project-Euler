def isPal(n):
    num = str(n)

    if num[::-1] == num:
        return True
    else:
        return False


sum = 0
for i in range(1000000):
    if isPal(i) and isPal(int(bin(i)[2:])):
        sum += i

print(sum)
