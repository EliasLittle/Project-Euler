###################
# Formatting Keys #
###################

file = open(r'/Users/EliasL/Documents/Code/Project Euler/Euler79/Euler79.txt')

key_set = []
for line in file:
    if int(line[:3]) not in key_set:
        key_set.append(int(line[:3]))

password = []
for i in str(key_set[0]):
    password.append(int(i))
del key_set[0]

######################
# Defining Functions #
######################


def indices(key):
    # Returns the indices of each character in key in the password
    keyed = [int(i) for i in str(key)]
    inds = [password.index(i) for i in keyed]
    return inds


def check(key):
    # Checks if each character is in the correct spot within the password
    a1, a2, a3 = indices(key)
    if a1 < a2 < a3:
        return True
    else:
        return False


def addToPass(key):

    skey = str(key)
    # contained: All digits already in password
    contained = [i for i in skey if int(i) in password]
    # nums: All digits to be added to password
    nums = [int(i) for i in skey if i not in contained]

    if len(nums) == 0:
        if not check(key):
            a1, a2, a3 = indices(key)
            if a2 < a1:
                password[a2], password[a1] = password[a1], password[a2]
                a1 = a2
                a2 = a1
            if a3 < a1:
                password[a3], password[a1] = password[a1], password[a3]
                a1 = a3
                a3 = a1
            if a3 < a2:
                password[a3], password[a2] = password[a2], password[a3]
            # print("Key: ", key, ":", check(key))
    else:
        for c in nums:
            if all([skey.find(str(c)) < skey.find(val) for val in contained]):
                password.insert(0, c)
            elif all([skey.find(str(c)) > skey.find(val) for val in contained]):
                password.append(c)
            elif len(contained) == 2:
                # print("insert", key)
                if contained[0] > contained[1]:
                    left = skey.find(contained[1])
                else:
                    left = skey.find(contained[0])
                password.insert(left+3, c)


############
# Run Code #
############


run = True
i = 0
while len(key_set) > 0:
    try:
        key = key_set[i]
    except:
        break

    remove = False
    if any(int(s) in password for s in str(key)):
        remove = True
        addToPass(key)
    if remove:
        key_set.remove(key)
    else:
        i += 1

print(password)
