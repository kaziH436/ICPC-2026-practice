# https://open.kattis.com
k=int(input())
initial={}
res=[]
for i in range(k):
    val=int(input())
    initial[val]=initial.get(val, 0)+1
    
requests=int(input())

# to add a key and value
initial[0]=initial.get(0, 0)+requests*3

for i in range(10):
    count=initial.get(i,0) # key 
    pairs=count//2
    remaining_zeros=count%2
    initial[i]=remaining_zeros
    initial[i+1]=initial.get(i+1,0)+pairs

for key in initial: # for i in range requires a numeric input
    if initial[key] == 1:
        res.append(key)

res.sort()
print(*res)
    
    
    
    
    