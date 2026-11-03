n=int(input())
arr=list(map(int, input().split()))
hash={}

for i in arr:
    # if arr[i+1]==arr[i]:
    #     count+=1
    # if count!=i:
    #     arr.remove(i)
    #     count-=1
    hash[i]=hash.get(i,0)+1
    
remove=0
for key, value in hash.items():
    if key<=value:
        remove+=value-key
    else:
        remove+=value
    # if key == None: done auto
    #     remove key?
    #     remove+=1
print(remove)
    