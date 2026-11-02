# 2n,  each n

# n turns for n cards 

# higher wins for all n cards
from itertools import permutations 

n=int(input())
resA=[]
resO=[]
for i in range(n):
    resA.append(int(input()))

# if alice has 2 5 4 
# the other person has 2*n - 2 5 4 
# 1 3 6 

# 1 min: 1 
# 2 max: 5 
# 1 min: 4
for i in range(1, 2*n+1):
    if i not in resA:
        resO.append(i)

w=[]

# resA=permutations(resA)
# resO=permutations(resO)
# for i in range(len(resA)):
#     for j in range(len(resO)):
for i in permutations(resA):
    for j in permutations(resO):
        wins=0
        for k in range(n):
            if i[k] > j[k]:
                wins+=1
        w.append(wins)
print(min(w), max(w))



