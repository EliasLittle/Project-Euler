import functions as f

'''
for i in f.prime_generator(987654321):
    print(i)
'''

for p in f.prime_generator(987654321):
    # print(p)
    if f.isPandigital(p):
        print(p)
        break
