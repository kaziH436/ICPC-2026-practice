# green 1 3 10 
# red 9 

# optimal: greedy?


# green 1 3 10 
# red 9 

# optimal: greedy?

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


# arr=list(map(int, input().split()))
# g=arr[0]
# r=arr[1]

# if g==0:
#     print(0)
#     exit()

# total=0
# currg=g
# currr=r

# if r <= g:
#     for i in range(r):
#         if currr >=0 and currg>=0:
#             total+=10
#             currg-=1
#             currr-=1
#     #remaining=currg
#     if currr >=0 and currg>=0 and  currg >=3: # elif only executes once
#         total+=10
#         currg-=3
#     if currr >=0 and currg>=0  and currg >=2:
#         total+=3
#         currg-=2
#     if currr >=0 and currg>=0  and  currg >=1:
#         total+=1
#         currg-=1

# if r > g: 
#     for i in range(g):
#         if currr >=0 and currg>=0:
#             total+=10
#             currg-=1
#             currr-=1
#     groups=currg//3
#     if currr >=0 and currg>=0  and currr >=3:
#         total+=groups*10
#         currr-=3
#     currg%=3
#     if currr >=0 and currg>=0  and currr >=2:
#         total+=groups*10
#         currr-=2
#     if currr >=0 and currg>=0  and currr >=1:
#         total+=groups*10
#         currr-=1


# print(total)
