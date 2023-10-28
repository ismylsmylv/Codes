s="abcdbakyeda"             #a3 b2 c1 d2 e1 k1 y1
def count(n):
    k=0
    for i in s:
        if i==n:
            k=k+1
    return(k)
for p in s:
    print(p,"=>", count(p))