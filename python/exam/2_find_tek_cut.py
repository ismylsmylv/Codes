n=int(input())
tek=0
cut=0
while n>0:
    if n%2==1:
        tek=tek+1
    if n%2==0:
        cut=cut+1
    n=n//10
print(tek, cut)