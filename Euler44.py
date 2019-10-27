# UNSOLVED
def Pn(n): return n*(3*n-1)//2


pents = list(map(Pn, list(range(1, 10000))))

answers = []
for i in range(len(pents)-1, 1, -1):
    for j in range(0, i):
        pi, pj = pents[i], pents[j]
        if pi+pj in pents and pi-pj in pents:
            answers.append([pi, pj])

print(answers)
