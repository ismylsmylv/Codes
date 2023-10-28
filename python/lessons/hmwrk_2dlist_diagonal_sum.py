cem=[0]
a=[[56 ,34, 23], [98, 51, 69], [29, 53, 12]]
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            cem[0]=cem[0]+a[i][j]
#            cem.append(a[i][j])
#cem.remove(0)
print("Elements on diagonal:",cem, "Sum is:", sum(cem))