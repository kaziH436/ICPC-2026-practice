# https://open.kattis.com/problems/stardustcurry

# Allocate pushups proportionally to the duration of each break.
def pushups():
    t=int(input())
    
    for i in range(t):
        d=list(map(int, input().split()))
        ti=list(map(int, input().split()))
    
        rate=d[1]/sum(ti)
        stress=0
        for i in range(len(ti)):
            p=rate*ti[i]
            stress+=p**2/ti[i] # syms of units of stress
    
        print(stress)
    # n breaks 
    # each i lasts for ti -> s
    # x pushups
    # x^2/s stress
    # derivative: -4x/s**3
    

pushups()
