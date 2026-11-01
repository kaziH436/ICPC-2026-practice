
# https://open.kattis.com/submissions/20776428
def mingle(n):
    
    # n rooms circle ordered 
    # n players target with same no.
    # distorientation k
    players = n[0]
    k = n[1]
    rooms=(2*k)+1
    ex=0
    player=0
    mod=998244353
    m=pow(rooms, mod-2, mod) # 1/rooms
    # player+=(1/rooms) * (1- 1/rooms)**(2*k) * rooms * players
    player = m  * pow((1 - m) % mod, 2*k, mod) * rooms * players
    ex+=player
    ex%=mod
    
    # 2k+1 =3  
    # player = 1
    # k = 1
    # 11 rooms 
    # player 1 enters room 5+1=6
    # addition=or 
    # multiplication = and 
    
    return ex

n=list(map(int, input().split()))
print(mingle(n))