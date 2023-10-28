n=100
S=0
for i in range(1, n+1):
    if i%2==0:              #for "cut"
        print(i)
        S=S+i
print("sum=", S)

n=100
S=0
for i in range(1, n+1):
    if i%2!=0:              #for "tek"
        print(i)
        S=S+i
print("sum=", S)

n=100
S=0
for i in range(1, n+1):
    if i%10==7:             #7 ile biten
        print(i)
        S=S+i
print("sum=", S)

n=100
S=0
for f in range(1, 101):
    k=i
    while k>10:
        k=k//10
    if k==7:
        print(k)
        S=S+i
print(S)
