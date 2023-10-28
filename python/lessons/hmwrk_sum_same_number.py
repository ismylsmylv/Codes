n=int(input("Enter number"))
s=0
sum=0
d=0
c=0
while s<=n:
    d=n//10
    c=c+d
    if c%2!=0:
        print(c-1)
        sum=sum+s
    s=s+1
print("son", sum)