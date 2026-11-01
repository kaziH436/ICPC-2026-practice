# https://open.kattis.com/problems/babyshark

# doo 6 

word=input().lower().split()

# hash={} storing the words with its positions

count=1
max_count=1
res=word[0]
for i in range(len(word)-1):
    if word[i+1]!=word[i]:
        count=1
    else:
        count+=1
        # max_count=max(max_count, count)
        if count > max_count:
            max_count=count
            res=word[i]
    
print(res)