n=int(input())
k=0
f=False
sum=0
i=n
for i in range(n):
    j=n%10
    sum=sum+j
    n=n//10
if sum==5:
    if n%10==5 or n%10==0:
        print(i)
    else:
        print("not")
print(sum)