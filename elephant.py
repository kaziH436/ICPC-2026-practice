import math 
m,d=input().split()

m=int(m) # total mg
d=int(d) # cleanup mg

# p=total peanuts

p=math.ceil(d/m)

print(p)

