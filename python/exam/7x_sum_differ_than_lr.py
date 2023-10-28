def firstDigit(n) :
    while n >= 10:
        n = n / 10;
    return int(n)
def lastDigit(n) :
    return (n % 10)
n=int(input())
last=n
print(firstDigit(n)+lastDigit(n))
s=0
last=n-(firstDigit(n)+lastDigit(n))
while last:
    s=s+last%10
    last=last//10
print(last)