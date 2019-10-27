def f(num, max):
    result = ''
    for i in range(1, max+1):
        result += str(num*i)
    return result


def isPan(num):
    if len(num) != 9:
        return False
    for i in range(1, 10):
        if str(i) not in num:
            return False
    return True


run = 9765

while run > 1:
    if isPan(f(run, 2)):
        print(f(run, 2))
        break
    else:
        run -= 1
