n=int(input())
arr=[]

no_open=True
valid=True
# blockers=False
for i in range(n):
    row = list(input())
    arr.append(row)
        
for i in range(len(arr)):
    for j in range(len(arr[i])):
        
        if arr[i][j] == '?':
            # Right
            for k in range(j + 1, len(arr[i])):
                if arr[i][k] in ['X', '0', '1', '2', '3', '4']:
                    break
                if arr[i][k] == '?':
                    valid = False
                    break
            
            # Left
            for k in range(j - 1, -1, -1):
                if arr[i][k] in ['X', '0', '1', '2', '3', '4']:
                    break
                if arr[i][k] == '?':
                    valid = False
                    break
            
            # Down
            for k in range(i + 1, len(arr)):
                if arr[k][j] in ['X', '0', '1', '2', '3', '4']:
                    break
                if arr[k][j] == '?':
                    valid = False
                    break
            
            # Up
            for k in range(i - 1, -1, -1):
                if arr[k][j] in ['X', '0', '1', '2', '3', '4']:
                    break
                if arr[k][j] == '?':
                    valid = False
                    break
        
        # every Every open cell is lit, 
        if arr[i][j] == '.':
            no_open=False
            lit=False
            # solution: bulb will lit unless blocked or out of bound
            for k in range(j + 1, len(arr[i])):
                if arr[i][k] == 'X' or arr[i][k]=='0' or arr[i][k]=='1' or arr[i][k]=='2' or arr[i][k]=='3' or arr[i][k]=='4':
                    break
                if arr[i][k] == '?':
                    lit=True

                    
            for k in range(j-1, -1,-1):
                if arr[i][k] == 'X' or arr[i][k]=='0' or arr[i][k]=='1' or arr[i][k]=='2' or arr[i][k]=='3' or arr[i][k]=='4':
                    break
                if arr[i][k] == '?':
                    lit=True
                    
            for k in range(i+1, len(arr)):
                if arr[k][j] == 'X' or arr[k][j]=='0' or arr[k][j]=='1' or arr[k][j]=='2' or arr[k][j]=='3' or arr[k][j]=='4':
                    break
                if arr[k][j] == '?':
                    lit=True
            
            for k in range(i-1, -1,-1):
                if arr[k][j] == 'X' or arr[k][j]=='0' or arr[k][j]=='1' or arr[k][j]=='2' or arr[k][j]=='3' or arr[k][j]=='4':
                    break
                if arr[k][j] == '?':
                   lit=True
            if not lit:
                valid=False

        if arr[i][j] == '0':
            count = 0
        
            if j + 1 < len(arr[i]) and arr[i][j+1] == '?':
                count += 1
            if j - 1 >= 0 and arr[i][j-1] == '?':
                count += 1
            if i + 1 < len(arr) and arr[i+1][j] == '?':
                count += 1
            if i - 1 >= 0 and arr[i-1][j] == '?':
                count += 1
        
            if count != 0:
                valid = False
        
        
        if arr[i][j] == '1':
            count = 0
        
            if j + 1 < len(arr[i]) and arr[i][j+1] == '?':
                count += 1
            if j - 1 >= 0 and arr[i][j-1] == '?':
                count += 1
            if i + 1 < len(arr) and arr[i+1][j] == '?':
                count += 1
            if i - 1 >= 0 and arr[i-1][j] == '?':
                count += 1
        
            if count != 1:
                valid = False
        
        
        if arr[i][j] == '2':
            count = 0
        
            if j + 1 < len(arr[i]) and arr[i][j+1] == '?':
                count += 1
            if j - 1 >= 0 and arr[i][j-1] == '?':
                count += 1
            if i + 1 < len(arr) and arr[i+1][j] == '?':
                count += 1
            if i - 1 >= 0 and arr[i-1][j] == '?':
                count += 1
        
            if count != 2:
                valid = False
        
        
        if arr[i][j] == '3':
            count = 0
        
            if j + 1 < len(arr[i]) and arr[i][j+1] == '?':
                count += 1
            if j - 1 >= 0 and arr[i][j-1] == '?':
                count += 1
            if i + 1 < len(arr) and arr[i+1][j] == '?':
                count += 1
            if i - 1 >= 0 and arr[i-1][j] == '?':
                count += 1
        
            if count != 3:
                valid = False
        
        
        if arr[i][j] == '4':
            count = 0
        
            if j + 1 < len(arr[i]) and arr[i][j+1] == '?':
                count += 1
            if j - 1 >= 0 and arr[i][j-1] == '?':
                count += 1
            if i + 1 < len(arr) and arr[i+1][j] == '?':
                count += 1
            if i - 1 >= 0 and arr[i-1][j] == '?':
                count += 1
        
            if count != 4:
                valid = False
print(1 if valid else 0)
