s="abcd"
f=True
for i in range(len(s)-1):
    if s[i]>s[i+1]:
        f=False
if f:
    print("ascending")
else:
    print("not ascending")