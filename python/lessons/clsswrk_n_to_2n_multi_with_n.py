n=int(input())
s=0
for m in range(1, n+1):
    k=1
    for i in range(m, 2*m+1):
        k=k*i
    s=s+k
print(s)