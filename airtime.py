# https://open.kattis.com/problems/airtime


# ai ai+1 ai+2 ti ti+1 ti+2 
# slope = x2-x1/y2-y1

n = int(input())
alt=[]
air=0
for i in range(n):
    a=int(input())
    alt.append(a)

for i in range(len(alt)-2): # for the last index
    m1=(alt[i+1]-alt[i])
    m2=(alt[i+2]-alt[i+1])
    
    
    if m1 > m2:
        air+=1
        
print(air)