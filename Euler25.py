a = 1
b = 0
n = 1

while len(str(a)) < 1000:
    a, b = a+b, a
    n+=1;
print (n)
