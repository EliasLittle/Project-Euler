from functions import isPalindrome

def lychrel(val, n=0):
    if isPalindrome(val) and n>0:
        return [True, val]
    if n >= 50:
        return [False,-1]
    s = str(val)
    return lychrel(int(s)+int(s[::-1]), n+1)

count = 0
for i in range(10000):
    if not lychrel(i,0)[0]:
        count+=1
print(count)
