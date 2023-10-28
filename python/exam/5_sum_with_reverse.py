num=int(input())
k=num
ters=0
while num!=0:
    d=num%10
    ters=ters*10+d
    num=num//10
print(k, ters, k+ters)