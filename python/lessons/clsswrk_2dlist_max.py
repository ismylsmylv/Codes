a=[[3, 5, 6], [63, 26, 78], [27, 83, 97]]
max=a[0][0]
for i in range (len(a)):
	for j in range(len(a)):
		if a[i][j]>max:
			max=a[i][j]
print(max)