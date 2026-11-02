arr = list(map(int, input().split()))
rows = arr[0]
cols = arr[1]
row = []
count = 0
locations = []

for i in range(rows):
    row.append(list(input()))

for i in range(len(row)):
    for j in range(len(row[i])):

        if row[i][j] == '0':
            if i - 1 >= 0 and i + 1 < len(row) and j - 1 >= 0 and j + 1 < len(row[i]):
                if (row[i-1][j] == 'O' and
                    row[i+1][j] == 'O' and
                    row[i][j+1] == 'O' and
                    row[i][j-1] == 'O' and
                    row[i-1][j+1] == 'O' and
                    row[i-1][j-1] == 'O' and
                    row[i+1][j+1] == 'O' and
                    row[i+1][j-1] == 'O'):

                    count += 1
                    locations.append((i + 1, j + 1))

if count == 1:
    print(*locations[0])
elif count > 1:
    print("Oh no!", count, "locations")
else:
    print("Oh no!")