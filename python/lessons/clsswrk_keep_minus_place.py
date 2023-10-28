a=[3, -2, 5, -4, 1]
j=0
for j in range (len(a)):
	f=True
	for j in range(len(a)-1):
		if a[j]>0 and a[j+1]:
			t=a[j]
			a[j]=a[j+1]
			a[j+1]=t
			f=False
	if f==True:break
print(a)