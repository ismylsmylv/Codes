a=[13, 22, 33, 45, 103]
def mainlist(n):
	f=False
	while n>0:
		if n%10==3:
			f=True
		n=n//10
	return f
print(mainlist(35))