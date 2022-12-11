import math
n=int(input("n="))
s=0
for i in range(1, n+1):
    t=n-i+1
    s=math.sqrt(t*3+s)
print(s)

#kok(2+kok(2+kok(2+)))
#kok(3+kok(3*2+kok(3*n+)))