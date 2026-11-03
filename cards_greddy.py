# 2n,  each n

# n turns for n cards 

# higher wins for all n cards
# from itertools import permutations 

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

# greedy appoach
# If both arrays are sorted in ascending order:
# - If Alice's current card is greater than Bob's current card, pair them and count a win.
# - If Alice's current card is less than or equal to Bob's current card, Alice can't win with that pairing. 
# Keep that Bob card in mind and try Alice's next card.

resA.sort()
resO.sort()
j=0
wins=0
loss=0
# maximum wins
for i in range(len(resA)):
    if resA[i] > resO[j]:
        wins+=1
        j+=1
    elif resA[i]<resO[j]:
        continue


# minimum wins 
resO.sort(reverse=True)
resA.sort(reverse=True)
k=0
for i in range(len(resA)):
    if resA[i] < resO[k]:
        loss+=1
        k+=1
    # elif resA[i]>resO[k]:
    #     k+=1
        # wins+=1
minimum_wins = n - loss

print(minimum_wins, wins)



