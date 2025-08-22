"""# sum of prices in the list
prices=[120,250,300,150,200]
sum=0
for i in prices:
    sum=sum+i
print("the sum of prices is:",sum)

#count and print the number of even and odd numbers in a list
numbers = [10, 25, 30, 47, 52, 61]
even_count=0
odd_count=0
even_list=[]
odd_list=[]
for i in numbers:
    if i%2==0:
        even_list+=[i]
        even_count+=1
    else:
        odd_list+=[i]
        odd_count+=1    

print(even_count, even_list)
print(odd_count, odd_list)

#finnding maximum value in the sequence of values
values=[32,35,30,36,34,31,33]
for i in values:
  x=max(values)
print(x)
#OR
values=[32,35,30,36,34,31,33]
max=0
for i in values:
  if i>max:
    max=i
print(max)
#enter username and password and login succesful if they enter more than 3 times print"acc is locked"
for i in range(3):
    user_name=input('enter your username:')
    pass_word=input('enter your password:')
    if (user_name=="admin") and (pass_word=="admin123"):
        print('Log in Successful!!!')
        break
    else:
        print('Wrong Credentials, Try again!')
else:
    print('Too many wrong attempts, Account Locked!')

#write a program to print discount of 100rs to passengers with seat numbers which are divisible by 3 and 5
seatnumbers=[5,25,13,15,27,55,11,30]
for i in seatnumbers:
 if i%3==0 and i%5==0:
    print("discount of 100rs to passengers :",i)
#to check the item is present in the store or not
items=input("enter your items")
if 'apple' in items or 'banana'in items or "capsicums"in items or "bread " in items or "onions" in items:
   print("the items are present")
else: 
   print("the items are not present")

#1. Print reverse of a string(without built in function).
string="jyothika"
for i in str:
    x=str[::-1]
print(x)

# 2. Average of marks of five students   marks=[400, 450, 530, 550, 570]
marks=[400, 450, 530, 550, 570]
for i in marks:
    avg=sum(marks)/len(marks)
print(avg)

# 3 check whether the given sides form a triangle or not:a=5, b=5, c=5 (Triangle rule: sum of any two sides is greater than the third side)
a,b,c=5,5,5
if a+b>c or b+c>a or c+a>b:
        print("the three sides are equal it is a triangle")
else:
        print("not a triangle")
"""
#factorial of a number
"""n=int(input ("enter a number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)"""
    
"""n=input ("enter a number:")
sum=0
for i in n:
    sum+=int(i)
print(sum)"""

"""n=input ("enter a number:")
a,b=0,1
print("fibonacci series")
for i in range(5):
    print(a,end="")
    a,b=b,a+b"""

"""n=input ("enter a number:")
count=0
for i in n:
    count+=1
print(count)"""

"""n=int(input ("enter a number:"))
sum=0
for i in str(n):
    sum+=int(i)
print(sum)"""

"""n=int(input ("enter a number:"))
count=0
for i in str(n):
    count+=1
print(count)"""

"""n=int(input("enter a number:"))
a=n**(1/2)
print("the perfect square :",a)
"""
"""a=int(input("enter a number:"))
root=a**0.5
if root==int(root):
    print("the num is a perfect square")
else:
    print("not a perfect square")"""

"""a=int(input("enter a number:"))
root=a**0.5
if a==root*root:
    print("the num is a perfect square")
else:
    print("not a perfect square")"""

"""n=int(input("enter a number:"))
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)"""

"""n=input("enter a number:")
count=0
for i in str(n):
    count+=1
print(count)"""

"""n=int(input("enter a number:"))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)"""

"""n=int(input("enter a number:"))   
rev=0
num=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10

if num==rev:
    print("palindrome")
else:
    print("not a plindrome")"""


string="jyothika"
rev=""
for ch in string:
    rev=ch+rev
print(rev)