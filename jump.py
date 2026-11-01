# https://open.kattis.com/problems/triplejump

# triple jump and total distance 
# need to find the three integer jumps and the total distance 

def distance(n,d):
    jumps = [a, b, c]
    possible = set()

    for i in jumps:
        for j in jumps:
            for k in jumps:
                possible.add(i + j + k)

    return possible == d
        
n = int(input())
d = set(map(int, input().split()))

a = min(d) // 3
c = max(d) // 3
    
for b in range(a + 1, c):
    if distance(n,d):
        print(a, b, c)
        break




