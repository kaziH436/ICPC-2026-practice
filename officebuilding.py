
# greedy problem 
# rotate 90 max 3 times
arr=list(map(int, input().split()))
r=arr[0]
c=arr[1]

ages=[]
count=0
curr_min=float('inf')
for i in range(r):
    row=list(map(int, input().split()))
    ages.append(row)
    count+=sum(row) # sum all ages in the row

arr_floor=list(map(int, input().split()))
s=arr_floor[0]
t=arr_floor[1]
floor=[]
for i in range(s):
    floor.append(input())

for _ in range(4):
    for a in range(r-len(floor)+1):
        for b in range(c-len(floor[0])+1):
            cut=0
            # find best placement:
            for i in range(len(floor)):
                for j in range(len(floor[0])):
                    if floor[i][j] == '#':
                        cut+=ages[a+i][b+j] 
            curr_min=min(curr_min,cut)
            
            # 90
    rotate=[]
    for j in range(len(floor[0])): 
        new_floor_row=""
        for i in range(len(floor)-1, -1,-1):
            new_floor_row+=floor[i][j]
        rotate.append(new_floor_row)
    floor=rotate
print(count-curr_min)
                