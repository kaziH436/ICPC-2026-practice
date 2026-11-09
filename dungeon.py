n=int(input())
arr=list(map(int, input().split()))
hash={}

for i in arr:
    hash[i]=hash.get(i,0)+1
    
remove=0
for key, value in hash.items():
    if key<=value:
        remove+=value-key
    else:
        remove+=value
print(remove)
    