

n=int(input())
resA=[]
resO=[]
for i in range(n):
    resA.append(int(input()))

# if alice has 2 5 4 
for i in range(1, 2*n+1):
    if i not in resA:
        resO.append(i)
resA.sort()
resO.sort()
j=0
wins=0
loss=0
for i in range(len(resA)):
    if resA[i] > resO[j]:
        wins+=1
        j+=1
    elif resA[i]<resO[j]:
        continue
resO.sort(reverse=True)
resA.sort(reverse=True)
k=0
for i in range(len(resA)):
    if resA[i] < resO[k]:
        loss+=1
        k+=1
minimum_wins = n - loss

print(minimum_wins, wins)



