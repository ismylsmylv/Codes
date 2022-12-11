s="akitabbkitabckitab"
t="kitab"
k="jurnal"
for i in range(len(s)):
    if s[i:i+len(t)]==t:
        d=s.replace(s[i:i+len(t)], k)
print(d)