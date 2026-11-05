n,x,m=input().split()
n=int(n)
x=int(x)
m=int(m)

arr=[]
for i in range(m):
    r=int(input())
    arr.append(r)

arr.sort()
countc=0
for i in range(1,x):
    if i in arr:
        countc+=arr.count(i)

counta=0
for i in range(x,n+1):
    if i in arr:  # index error with arr[i]
        counta+=arr.count(i) # need to handle duplicates
        
print(min(countc,counta))
