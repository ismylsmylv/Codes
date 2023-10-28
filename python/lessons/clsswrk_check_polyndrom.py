s="amma"
f=True
for i in range(len(s)-1):
    if s[i]>s[len(s)-i-1]:
        f=False
if f:
    print("polyndrom")
else:
    print("not polyndrom")