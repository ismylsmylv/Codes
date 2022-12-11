cem=[0]
ust=[0]
a=[[56 ,34, 23, 46], [98, 51, 69, 78], [29, 53, 12, 35], [76, 10, 47, 98]]
for i in range(len(a)):
    for j in range(len(a)):
        if i==j and i!=0:
            cem[0]=cem[0]+a[i][j-1]
            print(cem)
            ust[0]=ust[0]+a[i-1][j]
            print(ust)
print("Sum is:", sum(cem), sum(ust))