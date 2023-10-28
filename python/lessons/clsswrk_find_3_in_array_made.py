a=[13, 22, 33, 45, 103]
def mainlist(n):
	f=True
	while n>0:
		if n%10==3:
			f=False
		n=n//10
	return f
for m in range (len(a)):
	print(mainlist(m))
	print(a[m])