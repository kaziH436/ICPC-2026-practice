# https://east.na.icpc.global/problems/2026/olp/E-Fractionalsequence/E-Fractionalsequence.pdf
import math
n=int(input())

i=1

while (i*(i+1))//2<n:
    i+=1
    
k=n-((i*(i-1))//2)-1
s=i+k/i

g=math.gcd(k,i) # k i in the fraction for s and finds great common divisor 

a=k//g
b=i//g

if k == 0:
    print(i)
else: 
    print(str(i)+" "+str(a)+'/'+str(b))

