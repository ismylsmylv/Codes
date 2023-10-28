n=int(input("enter a number"))
while n>1:
    print(n%2, end='')
    n=n//2
    if n%2==0:
        print(n%2, end='')
    else:
        print(n%2, end='')