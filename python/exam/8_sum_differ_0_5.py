n=int(input("enter"))
k=0
while n>0:
    m=n%10
    if m!=0 and m!=5:
        k=k+m
    n=n//10
print(k)