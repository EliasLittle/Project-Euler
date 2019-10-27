def polygonGen(fx):
    lst = []
    i = 1
    while fx(i) <= 9999:
        lst.append(int(fx(i)))
        i += 1
    return lst


tri = polygonGen(lambda x: x*(x+1)/2)
sqr = polygonGen(lambda x: x*x)
pnt = polygonGen(lambda x: x*(3*x-1)/2)
hex = polygonGen(lambda x: x*(2*x-1))
hpt = polygonGen(lambda x: x*(5*x-3)/2)
oct = polygonGen(lambda x: x*(3*x-2))

nums = [tri, sqr, pnt, hex, hpt, oct]


def clean(lst):
    newlst = lst
    length = len(newlst)
    i = 0
    while i < length:
        val = newlst[i]
        if val < 1000:
            newlst.remove(val)
            length -= 1
            i -= 1
        i += 1

    for i in range(len(newlst)):
        s = str(newlst[i])
        n = (s[:2], s[2:])
        newlst[i] = n
    return newlst


nums = list(map(clean, nums))

matches = set()


def pairs(lst1, lst2):
    for j in range(len(lst1)):
        val1 = lst1[j][0]
        for k in range(len(lst2)):
            val2 = lst2[k][1]
            if val1 == val2:
                matches.add(lst2[k])
                matches.add(lst1[j])


def recPairs(lst, value):
    ans = []
    for i in range(lst):
        test = []
        if value[1] == lst[i][0]:
            test.append(recPairs(lst.remove(value), lst[i][0]))
        ans.append(max(list(map(len, test))))
    return ans


for i in range(1, len(nums)):
    pairs(nums[i], nums[i-1])

print(recPairs(list(matches.remove(('39', '40'))), ('39', '40')))
