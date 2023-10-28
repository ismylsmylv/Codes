n=int(input("Enter number"))
m=int(input("Enter place"))
say=0
j=0
while n>0 and j<m:
    say=n%10
    n=n//10
    j+=1
print(say)
