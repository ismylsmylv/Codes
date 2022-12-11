import math

a=int(input("Enter a: "))

b=int(input("Enter b: "))

c=int(input("Enter c: "))

d=int(b*b-4*a*c)

if d>=0:
	x1=(-b-math.sqrt(d))/2*a
	x2=(-b+math.sqrt(d))/2*a
	print("x1 and x2 is:", x1, x2)
else:
	print("Cannot be solved")