n=int(input('Enter number'))
f=False
while n>0 and not f:
    if n%10==5:
        f=True
    n=n//10
print(f)