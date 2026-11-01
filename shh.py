# https://open.kattis.com/problems/regarde

# n  -> shh n+1 h's

def hush():
    t=int(input())
    
    for i in range(t):
        n=int(input())
        print("s"+"h"*(n+1))

    
hush()