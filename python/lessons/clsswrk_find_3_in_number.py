n=int(input('Enter number'))
f=False
while n>0 and not f:
    if n%10==3:
        f=True
    n=n//10
    if(f==True):
        print("included")
    else:
        print("not included")