import math 

# round up = math.ceil
# round down = math.floor

n=int(input())
arr=[]
for i in range(n):
    arr.append(float(input()))

for i in range(len(arr)):
    arr[i]=arr[i]*100
    last_d=arr[i]%10
    if last_d == 3 or last_d == 4 or last_d == 6 or last_d == 7: #add 6 n 7
        arr[i]=arr[i]-last_d # float and int comp Returns True
        # last_d=math.ciel(last_d)
        arr[i]=arr[i]+5
        arr[i]=arr[i]/100.0
        
    elif last_d == 8 or last_d ==9:
        arr[i]=arr[i]-last_d
        # last_d=math.ciel(last_d)
        arr[i]=arr[i]+10
        arr[i]=arr[i]/100.0
        # last_d=math.ciel(last_d) 

    elif last_d == 1 or last_d==2:
        arr[i]=arr[i]-last_d
        # last_d=math.ciel(last_d)
        # arr[i]=arr[i]
        arr[i]=arr[i]/100.00

    else: 
        arr[i]=arr[i]/100.00

for i in range(len(arr)):
    # print(arr[i])
    print(f"{arr[i]:.2f}")
