# https://open.kattis.com/problems/fairytale

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
                    if (low,high) in s:
                        continue
                    else:
                        strings+=1
                        s.add((low,high))
                    
        print(strings)
        
melody()            
            
        
