
all=list(map(int, input().split()))

n=all[0]
a=all[1]
b=all[2]

wordfb=0
wordf=0
wordb=0
for i in range(1,n+1):
    if (i % a)==0 and (i%b)==0:
        wordfb+=1
    elif (i % a)==0:
        wordf+=1
    elif (i%b)==0:
        wordb+=1
arr=[wordf,wordb,wordfb]
print(*arr)