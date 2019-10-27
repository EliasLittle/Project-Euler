#UNSOLVED... :(
from math import sqrt
import time


def f(D):
    x, y = 2, 1
    a = pow(x, 2) - D*pow(y, 2)
    while a != 1:
        while a > 1:
            y += 1
            a = pow(x, 2) - D*pow(y, 2)
        x += 1
        a = pow(x, 2) - D*pow(y, 2)
    return x


def k(D):
    x, y = 1, 1
    a = pow(x, 2) - D*pow(y, 2)
    add = True
    while a != 1:
        while a > 1:
            y += 1
            a = pow(x, 2) - D*pow(y, 2)
        if a != 1:
            if add:
                x += D-2
                a = pow(x, 2) - D*pow(y, 2)
            else:
                x += 2
                a = pow(x, 2) - D*pow(y, 2)
            add = not add
        else:
            return x
    return x


def g(D):
    x, y = 1, 1
    a = pow(x, 2) - D * pow(y, 2)
    large_add = True
    while a != 1:
        while a > 1:
            y += 1
            a = pow(x, 2) - D*pow(y, 2)
        if a != 1:
            if large_add:
                x += D-2
                a = pow(x, 2) - D*pow(y, 2)
            else:
                x += 2
                a = pow(x, 2) - D*pow(y, 2)
            large_add = not large_add
        else:
            return x
    return x


def h(D):
    x, y = int(sqrt(D)), 1
    a = pow(x, 2) - D * pow(y, 2)
    while a != 1:
        if pow(x, 2, D) == 1:
            while a > 1:
                y += 1
                a = pow(x, 2) - D*pow(y, 2)
            if a != 1:
                x += 1
                a = pow(x, 2) - D*pow(y, 2)
            else:
                return x
        else:
            x += 1
            a = pow(x, 2) - D*pow(y, 2)
    return x


print(k(5))

start = time.time()
max = 0
for i in range(74):
    if int(sqrt(i)) == sqrt(i) or i == 61:
        continue
    val = f(i)
    if val > max:
        max = val
end = time.time()
print("Time: "+str(end-start))


start = time.time()
max = 0
for i in range(74):
    if int(sqrt(i)) == sqrt(i) or i == 61:
        continue
    val = h(i)
    if val > max:
        max = val
end = time.time()
print("Time: "+str(end-start))

start = time.time()
max = 0
for i in range(74):
    if int(sqrt(i)) == sqrt(i) or i == 61:
        continue
    val = k(i)
    if val > max:
        max = val
end = time.time()
print("Time: "+str(end-start))
