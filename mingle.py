
# https://open.kattis.com/submissions/20776428
def mingle(n):
    
    players = n[0]
    k = n[1]
    rooms=(2*k)+1
    ex=0
    player=0
    mod=998244353
    m=pow(rooms, mod-2, mod) # 1/rooms
    player = m  * pow((1 - m) % mod, 2*k, mod) * rooms * players
    ex+=player
    ex%=mod
    
    return ex

n=list(map(int, input().split()))
print(mingle(n))