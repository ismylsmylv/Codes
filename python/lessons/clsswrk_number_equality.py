n=int(input())
f=False
while n>0 and not f:
	if n%10==n//10:
		f=True
	n=n//10
if (f==True):
		print("equal")
else:
		print("not")