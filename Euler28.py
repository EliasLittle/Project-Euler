sum, i, adder, stop = 0, 1, 2, pow(1001, 2)
while i <= stop:
    for n in range(4):
        sum, i = sum+i, i+adder
        if i > stop:
            break
    adder += 2
print(sum)
