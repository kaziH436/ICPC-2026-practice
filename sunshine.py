# https://open.kattis.com/problems/walkingonsunshine
arr=list(map(int, input().split()))
n=arr[0]
xc=arr[1]
yc=arr[2]
xa=arr[3]
ya=arr[4]

rec=[]
for i in range(n):
    row=list(map(int, input().split()))
    rec.append(row)

total=max(0,yc-ya)

intervals=[]

for i in range(n):
    low=max(ya,rec[i][1]) # higher of the two lower boundaries
    high=min(rec[i][3],yc) # lower of the two upper boundaries

    if low < high: # why? to get overlap
        intervals.append((low,high))

intervals.sort()

merged=[] 
for i in intervals:
    if not merged or i[0] > merged[-1][1]:
        merged.append([i[0], i[1]])
    else:
        merged[-1][1]=max(merged[-1][1], i[1])

shade=0
for i in merged:
    shade+=i[1]-i[0]

print(total-shade)