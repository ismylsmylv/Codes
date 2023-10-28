n=int(input("Enter number"))
s=0
t=n%10
f=True
while n>0:
    if n%10 !=t:    #if n%10 differ than n%10, it exits False
        f=False
    n=n//10
if f==True:
    print("Same")
else:
    print("Different")