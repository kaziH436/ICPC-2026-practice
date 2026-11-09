
from itertools import permutations 

n=int(input())
resA=[]
resO=[]
for i in range(n):
    resA.append(int(input()))
for i in range(1, 2*n+1):
    if i not in resA:
        resO.append(i)

w=[]
for i in permutations(resA):
    for j in permutations(resO):
        wins=0
        for k in range(n):
            if i[k] > j[k]:
                wins+=1
        w.append(wins)
print(min(w), max(w))



