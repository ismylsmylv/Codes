s="akitabbkitabckitab"
t="kitab"
k="jurnal"
p=""
i=0
while i<len(s):
	if s[i:i+len(t)]==t:
		p=p+k
		i=i+len(t)-1
	else:
		p=p+s[i]
	i=i+1
print(p)
		