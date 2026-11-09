
arr=list(map(int, input().split()))
g=arr[0]
r=arr[1]
total=0
currg=g
currr=r

if g==0:
    print(0)
    exit()

mixed=min(g,r)
total+=mixed*10
currg=g-mixed

groups=currg//3
total += groups * 10
currg %= 3 # remaining after making the groups or currg -= groups * 3

if currg >= 2: # maximize for 3 means the next number can be 0 1 2 not 2+2 =4 
    total += 3
elif currg >= 1:
    total += 1

print(total)
