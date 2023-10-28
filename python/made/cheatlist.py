#just some test codes by ismylsmylv

#####           Taking user input           #####
username = input ("Enter name: ")
age = input("Enter age: ")
print("Name: ", username , "\nAge: ", age)


#####           Addition of numbers         #####
integer_number=345 
float_number=34.5
sum= integer_number+float_number
print(sum, type(sum))


#####           Converting data types       #####
float_number=23.34
integer_number=int(float_number)
print(integer_number)
print(float_number)
print(type(float_number))
###   with float and int types   ###
float_number=1.234
integer_number=(int(float_number))
print(integer_number)
print(float_number)
###   from int and float to string   ###
a=39
b=23.23
str_a=str(a)
str_b=str(b)
print(str_a)
print(type(str_a))
print(str_b)
print(type(str_b))


#####           Multipyling data            #####
a="hello there "
b=a*743434
print(b)
###2**5 means 5th power of 2
print(2**5)


#####      if, elif and else statements     #####
number=float(input("Enter the number"))
if number >=0:
    print("Number is positive or equal to zero")
else:
         print("Number is negative")

#####             while loop                #####
###infinite output code loop
a=float(input("Enter number"))
while a!=0:
    print("hehe")
###sum of numbers
n=float(input("Enter quantity numbers: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print("The sum is: ", sum)

#####               for loop               #####
###   to list elements in brackets   
languages =["Java", "Python", "Javascript"]
for item in languages:
    print(item)
### sum of numbers with for loop ###
numbers = range (1, 101)
sum=0
for i in numbers:
    sum +=i
print("Sum =", sum)
###   multiplication table   ###
n=14
for i in range(1, 11):
    print(n, " x ", i, " = ", n*i)
else:
    print("Table completed")

#####            break in listing           #####
numbers=[1, 2, 54554, 54543423, -598598694, 390293049]
for val in numbers:
    if val<0:
        break
    print(val)
###   break in loop   ###
sum=0
while True:
    n=input("Enter a number: ")
    n=float(n)
    if n<0:
        break   #replacable with continue for negatives
    sum+=n
    print("Sum= ", sum)

#####    Flow controls with if/else/elif    #####
num1=5
num2=2
num3=-3
if(num1>=num2) and (num1>=num3):
    largest = num1
elif (num2>=num1) and (num2>=num3):
    largest = num2
else: largest = num3
print("Largest is: ", largest)

#####           Check prime numbers         #####
num=409
flag=1
for i in range(2, num):
    if (num%i)==0:
        print(num, "isn't prime")
        print(i, "times", num//i, "is",num)
        flag=0
        break
    if flag==1:
        print(num, "is prime number")

#####    Defining function using return     #####
def add_numbers(n1, n2):
    sum=n1+n2
    return sum
answer=add_numbers(14, 45)
print("sum=", answer)

#####    local and global scope difference    #####
def my_fun():
    x=5
my_fun()
#print(x)        #is an error code

#####           Lambda functions            #####
square= lambda x : x*x
a= input("Enter the number: ")
a=int(a)
result=square(a)
print ("Square of", a, "is", result)
###              or               ###
sum= lambda a, b, c: a+b+c
print(sum(4, 34, 546))

#####               Recursion               #####
def calc_sum(n):
    if n==1:
        return 1
    else:
        return n+calc_sum(n-1)
sum=calc_sum(3)
print(sum)

#####               Lists                   #####
numbers = [1, 4, 43, 675, 32, 45, 142]
print (numbers)
numbers = [1, 54, [398, 312]]  #nested list
print(numbers[5])   #place of element starting 0
print(numbers[-3])  #from right to left
print(numbers[2:5]) #multiple elements
numbers[2]=16       #changing element
numbers.append(67)  #adding new element by append
numbers.extend([55, 22, 11])    #adding new list
print(numbers+[654, 2345, 234]) #adding new ones
print(numbers*3)    #repeat items of list
numbers.insert(7, 34)   #adding 34 to 7th index
del numbers         #delete entire list
del numbers[-3]     #delete indexed item
del numbers[2:5]    #delete multiple at once
numbers.remove(2)   #delete indexed item
numbers=[2, 3, 4, 5, 6]
numerals=[1]
numbers=numerals    #copying list
print(numerals)
#####             Loop on list              #####
for fruit in ["apple", "banana", "berry"]:
    print("I like", fruit)

#####               Tuples                  #####
extuple=()                         #empty tuple
extuple=(1, 2, 3)                  #with elements
extuple=(1, 3.4, "Hello")          #mixed data
extuple=(2.5, [90, 12], (6, 7, 8)) #nested tuple
extuple=5, 6, 5.6, "random"        #without []
t1=("tuple test", )                #default one
t2=('q', 'w', 'e', 'r', 't', 'y')  #outputs same
print(t2[3:5]*4)
t2=('q', 'w', 'e', 'r', 't', 'y')   
result=t2.count('e')               #output is 1
result=t2.index('e')               #output is 2

#####               Strings                 #####
exstring='random string'
exstring="random string"
exstring='''random string'''
print(exstring)
print(exstring[4])     #printing special character
print(exstring[6:10])  #slicing
del exstring           #delete string
###         operations on strings           ###
first_name="John"
last_name="D'Claire"
print(first_name+" "+last_name)
print(first_name*8)
###              counting letters           ###
count=0
for letter in " Marvel's Multiverse of Madness":
    if (letter=="M"):
        count+=1
print(count, "letters found")

#####                 sets                  #####
random_set={5445, "Blah blah blah", (4.5, 6.7)}
print(random_set)
random_set.add(111)
random_set.update([990, 9299292, 9399339])
random_set.discard(5445)
random_set.remove("Blah blah blah")
print(random_set)

#####             set unions                #####
A={1, 2, 3, 4, 5, 6}
B={5, 6, 7, 8, 9 ,10}
print(A|B)                          #merge
print(A&B)                          #same elements
print(B.intersection(A))            #same elements
print(A-B)                          #difference
print(A.difference(B))              #difference
print(B-A)                          #difference
print(A^B)                          #sym difference
print(A.symmetric_difference(B))    #sym difference
print(A.union(B))
for element in set(A|B):            #as loop
    print(element)

#####              dictionary               #####
random_dict={}
random_dict={1: "Name", 2: "Surname"}
random_dict={"user": "John", 1: [3, 4, 5]}
random_dict=dict({1: "username", 2:"password"})
print(random_dict)
person={"name": "Jack", "age": 25}
person_name=person["name"]
person_age=person.get("age")
print(person_name, person_age)
person["salary"]=5000
person_salary=person["salary"]
print(person_name, person_age, person_salary)
person["salary"]=6000
value=person.pop("salary")
print("Removed:", value)
print(person)

#####               modules                 #####
def add(a, b):
    "This module adds two modules" 
    result=a+b
    return result
###save as seperate addition.py file to use ###
#import addition
#output.addition.add(34+17)
#math.sin(x); math.pow(x, y) are built-in
import math
a=math.e
print(a)
from math import pi      #import with from
print(pi)
import math              #list valid attributes
print(dir(math))

#####               files                   #####
f=open("helloworld.txt")         #to open file
f=open("helloworld.txt")
f=open("helloworld.txt", 'w')    #write mode
f.close()
#or
try:
    f=f=open("helloworld.txt")
finally:
    f.close()
#or
with open("helloworld.txt",'w', encoding ='utf-8') as f:
    f.write("random words")
    f.write("blah blah blah")
print(f.read(4))                #keep empty to read fully
for line in f:
    print (line)
print(f.readline())

#####              directories              #####
import os
os.mkdir('test')                #create directory
os.rename('test', 'updated')    #rename directory
os.rename('updated', "/home/ismylsmylv") #move file
os.listdir()                    #list directory
os.remove('old.txt')           #remove directory