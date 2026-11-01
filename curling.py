# https://open.kattis.com/problems/curling



# 144,84
# 10 times
# distance formula (x2-x1)^2 + (y2-y1)^2

# number of stones that remain on the ice sheet
# x y coordinates 
def game():
    pointsr=0
    pointsy=0
    for i in range(10):
        n=list(map(int, input().split()))
        m=list(map(int, input().split())) 
        diffred=[]
        diffyellow=[]
            
        for i in range(1, len(n)-1, 2):
            # 1627 63 for red
            # 1506 128 for yellow
            diffr=(n[i]-144)**2 + (n[i+1]-84)**2
            diffred.append(diffr)
            
        for j in range(1, len(m)-1, 2):
            diffy=(m[j]-144)**2 + (m[j+1]-84)**2
            diffyellow.append(diffy)
        
        if diffred and diffyellow:
            # if min(diffred) < min(diffyellow):
            for i in range(len(diffred)):
                if diffred[i] < min(diffyellow):
                    pointsr+=1
            # elif min(diffyellow) < min(diffred):    
            for i in range(len(diffyellow)):
                if diffyellow[i] < min(diffred):
                    pointsy+=1
        elif diffred:
            pointsr+=len(diffred)
            
        elif diffyellow:
            pointsy+=len(diffyellow)
    
    print(pointsr, pointsy)
    
game()
    
