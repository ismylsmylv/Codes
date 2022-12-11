a=int(input("a"))
say=0
max=0
while a>0:
	say=a%10
	if say>max:
		max=say
	a=a//10
print(max)
	