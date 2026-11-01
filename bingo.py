# https://open.kattis.com/problems/tenplayerbingo


# 1-10 players
# each receive from 1-100 of there last digit 
# each will be 10 digits? 

# game master gets 1-100 unique and shuffled 



def game(nums):
    hash = {}
    for i in range(len(nums)):
        last=nums[i]%10
        # if last not in hash:
        hash[last]=i
    winner=max(hash, key=hash.get)
    if winner == 0:
        return 10
    else:
        return winner 
        
nums=list(map(int, input().split()))
print(game(nums))