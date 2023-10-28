n=100
S=0
for i in range(1, n+1):
	k=i
	while k>10:
		k=k//10
	if k==7:
		S=S+i
print (S)