n=int(input())
k=False
for i in range(n):
    j=n%10
    if j%2==0:
        k=True
    n=n//10
    if k==True:
        print(i)