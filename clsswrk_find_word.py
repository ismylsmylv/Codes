s="akitabgfjfjnkitabjsslkkitab"
t="kitab"
k=0
for i in range(len(s)):
    if s[i:i+len(t)]==t:
        k=k+1
print(k)