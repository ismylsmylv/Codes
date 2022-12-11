n=int(input("Enter number"))
say=0
while n>0:
    say=say+n%10
    n=n//10
print(say)