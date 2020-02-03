triangle = open('Euler67.txt','r')
stringArr = [line.split() for line in triangle]

arr = [map(int, x) for x in stringArr]

def max(a,b):
    return a if a > b else b

def solver(x):
    for i in range(0,len(arr[x])):
        arr[x][i] = arr[x][i] + max(arr[x+1][i],arr[x+1][i+1])

for j in range(len(arr)-2,-1,-1):
    solver(j)

print(arr[0][0])
