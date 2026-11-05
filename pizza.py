pizza = {
    "S": 0, 
    "M": 0,
    "L": 0,
} # easy to have prepopulate dict

n = int(input())

for i in range(n):
    size, left=input().split()
    pizza[size]=pizza.get(size,0)+int(left)

res=0
res+=(pizza['S'])//6
res+=(pizza['M'])//8
res+=(pizza['L'])//12

if pizza['S'] % 6 !=0:
    res+=1
    
if pizza['M'] % 8 !=0:
    res+=1
    
if pizza['L'] % 12 !=0:
    res+=1

print(res)