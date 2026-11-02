#tungsten and gold, all coins same size and color
# modern penny scale and 1 penny

# penny scale: 1. penny and objects 
# 2. displays weight tp mg

# tungstem: 29 260 mg
# gold: 29 370 mg

arr=list(map(int,input().split()))

w=arr[0]
s=arr[1]
c=(s*(s+1))//2

for i in range(1,c+1):
    curr=29260*(c-i)+29370*i
    if curr==w:
        print(i)