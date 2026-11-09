# https://open.kattis.com/problems/tenplayerbingo


def game(nums):
    hash = {}
    for i in range(len(nums)):
        last=nums[i]%10
        hash[last]=i
    winner=max(hash, key=hash.get)
    if winner == 0:
        return 10
    else:
        return winner 
        
nums=list(map(int, input().split()))
print(game(nums))