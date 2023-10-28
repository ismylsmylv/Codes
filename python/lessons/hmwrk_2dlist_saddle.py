a=[[1, 2, 3,] ,[4, 5 ,6], [7, 8, 9]]
max=a[0][0]

for i in range(len(a)):
    for j in range(len(a)):
        if a[i-1][j-1]>=a[i][j] and a[i-1][j-1]<=a[i][j]:
            max=a[i-1][j-1]
print(max)