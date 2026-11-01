# https://open.kattis.com/problems/espressomacchiato


# n*n
# right down

# each has a coffee shop or no, the start and end can't

test=int(input())

for t in range(test):
    n=int(input()) # n*n
    
    for i in range(n):
        row=""
        for j in range(n):
            if (i,j) != (0,0) and (i,j) != (n-1,n-1) and (i+j)==n-1:
                row+="C"
            else:
                row+="."
        print(row)

    