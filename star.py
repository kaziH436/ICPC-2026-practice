# https://open.kattis.com/problems/starguardians
# each no. of pronlems 
# size = additional 


# output max = avg of p/ member 

def problems(n, a, s):
    avg=[]
    totals=0
    s.sort(reverse=True) # important when team size is 1
 # number of problems each Star Guardian
    for i in range(len(a)):
        totals+=s[i]
        average=(a[i]+totals) /(i+1)
        avg.append(average)

    return max(avg)

n=int(input()) # number of possible teams
a=list(map(int, input().split())) # the additionals if team is 1 2 etc
s=list(map(int, input().split())) # each member can solve 

print(problems(n,a,s))

