file = open(r'/Users/EliasL/Documents/Code/Project Euler/Euler89/Euler89.txt')

numArr = [line[:-1] for line in file]
subs = ["DCCCC", "LXXXX", "VIIII", "CCCC", "XXXX", "IIII"]
savedchars = 0

for str in numArr:
    num = str
    oglen = len(str)
    for i in subs:
        if i in str:
            num = num.replace(i, "aa")
    savedchars += (oglen-len(num))

print(savedchars)
