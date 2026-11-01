# https://open.kattis.com/problems/fairytale

# 4 
# each : 1-10

def melody():
    t=int(input())
    for i in range(t):
        n=int(input())
        pitch=list(map(int, input().split()))
        
        strings=0
        hash={
            1: (1,10),
            2: (11,20),
            3: (21,30),
            4: (31,40)
        }
        s=set()
        for p in pitch:
            for string, interval in hash.items():
                low,high=interval # unpack the tuple
                
                
                if low<=p<=high: 
                    # You don't need to check all previously encountered intervals manually. A set can do that for you.
                    if (low,high) in s:
                        continue
                    else:
                        strings+=1
                        # avoid dupe counting
                        s.add((low,high))
                    
        print(strings)
        
melody()            
            
        
