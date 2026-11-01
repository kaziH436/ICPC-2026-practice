# https://open.kattis.com/problems/eviljudges

# swap to ensure AC and AK aren't together, and order msut be Ak or AC
# adjacent

# s=list(input())
s=input()
m = int(input())

def count_sub(s):
    a=0
    ak=0
    ac=0
    for i in s:
        if i=='A':
            a+=1
        elif i=='C':
            ac+=a
        elif i=='K':
            ak+=a
    return ac+ak
    
best=count_sub(s)
print(max(0, best - m))

# for i in range(len(s)-1):
    # before swaping 
    # best=count_sub(s)
    # before=s.copy()
    
    # if m > 0:
    #     s[i],s[i+1]=s[i+1], s[i]
    #     totala=count_sub(s)
    #     after=s.copy()
        
    #     if best>totala:
    #         m-=1
    #         s=after
    #         best=totala
    #     else:
    #         s=before

# print(best)
        
        