n=int(input())
cem=0
m=0
dovr=0
while m<=dovr:
	m=n//10
	m=m+1
for i in range (0, m):
	cem=cem+n%10
	n=n//10
print(cem)