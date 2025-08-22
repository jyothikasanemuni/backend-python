"""a="j"
b="y"
c="o"
print(a+"\n"+ b+"\n"+ c+"\n") # name in vertical
print (c+"\n"+ b+ "\n"+ a + "\n") # same name but reverse""" 

# type casting
"""a=8.354
b=(type(a))
print(b)"""

# SWAPPING OF NUMBERS 
# EXAMPLE 1
"""a=2
b=3
c=0

c=a #2
a=b #3
b=c #2
print(a)
print(b)"""

# EXAMPLE 2
"""a=1
b=2
c=3
d=0

d=a
a=b
b=c
c=d

print (a)
print(b)
print (c)"""

# Print numbers from 1 to 10 using a for loop.

'''list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)'''

#Print each character in the word "banana" using a for loop.
"""string="banana"
for i in string:
    print(i)
"""
#Print the squares of numbers from 1 to 5 using a for loop.

"""for i in range (0,6):
    print(i**2)
"""
# Print all even numbers in the list: [2, 5, 8, 9, 10].
"""list=[2, 5, 8, 9, 10]
for i  in list:
    if i % 2==0:
     print(i)"""

#Print numbers from 1 to 20 that are divisible by 3 using a for loop.
"""num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in num:
    if i%3 ==0:
        print(i)"""

# Print multiplication table of 2 using a for loop (up to 10 times)
"""for i in range(1,11):
    print("2 X",i ,"=", 2 * i)"""

#nested while loop
"""i = 3 # rows
while i > 0:
    j = 3 #columns
    while j > 0:
        print("*",end=" ")
        j = j - 1
    print() 
    i = i - 1"""


# reverse of a string or number
'''x=(input("enter a number or string:"))
y=x[::-1]
print(y)'''

#Print numbers from 1 to 5 using a while loop.
"""i=1
while i<=5:
    print(i)
    i=i+1"""

#Print even numbers from 1 to 10 using a while loop.
"""i=1
while i <= 10 :
    if i%2==0:
     print(i)
    i=i+1"""

#Print the sum of numbers from 1 to 10 using a while loop.
'''i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print(sum)
'''
# Print numbers from 10 down to 1 using a while loop
"""i=10
while i>0:
    i=i-1
    print(i)"""

#Print the word "Hello" 5 times using a loop.
"""i=1
while i<=5:
    print("hello")
    i=i+1"""

#Ask the user their favorite color 3 times using a loop.
'''i=1
while i<=3:
    color=(input(f"favourite color {i}:"))
    print("favorite color is:", color)
    i=i+1
'''

#Print numbers from 1 to 10 and print "Even" or "Odd" next to each.
"""i=1
while  i<=10:
    if i%2==0:
        print("even")
    else:
        print("odd")
    i=i+1"""
# sum of digits
"""num=int(input("enter a number:"))

total=0

while num > 0:
    digit=num%10
    total=total+digit
    num=num//10
print("sum of digits:",total)"""


# to check sum 0f middle digits is equal to sum of first and last digits 
"""
# Step 1: Take input from user
number = input("Enter a number: ")

# Step 2: Convert each character into an integer digit
digits = [int(d) for d in number]

# Step 3: Extract first and last digit
first = digits[0]
last = digits[-1]

# Step 4: Get middle digits (excluding first and last)
middle_digits = digits[1:-1]

# Step 5: Calculate sums
sum_first_last = first + last
sum_middle = sum(middle_digits)

# Step 6: Compare and print result
if sum_first_last == sum_middle:
    print("equal")
else:
    print("not equal")
"""

#Ask the user to enter 5 numbers and print only the even numbers
"""a="banana"
b=0
for i in a:
    if i ==a:
        b=b+1
        print(b)
print("banana in a aare:",b)"""

#vowels
"""word = input("Enter a word: ")
count=0
for a in word:
    if a.lower() in "aeiou":
        print("vowel:" ,a)"""


# nested ternary loop

"""marks=int(input("enter a marks:"))
print("grade O" if marks>=95 else "grade A" if marks>=85 else "grade B" if marks >=75 else "grade C" if marks >=50 else "grade D" if marks >=35 else "fail")
"""
#check if array is sorted or not
"""def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]< arr[i+1]:
            return True
    return False
arr=[1,2,3,4,5]
print("sorted array is :", is_sorted(arr))"""

#removing duplicates from the array
"""def removing_duplicates(arr):
    result=[]
    for num in arr:
        if num not in result:
            result.append(num)
    return result
arr=[1,2,3,4,2,2,4,5,4,3]
print("after remmoving duplicates from the array:", removing_duplicates(arr))
"""



# finding the largest num in array
"""def find_largest(arr):
    largest=arr[0]
    for num in arr:
        if num>largest:
           largest=num
        
    return largest
 
arr=[2,9,2,15,5,7]
print("largest number is:", find_largest(arr))"""

# reverse of an array
"""def reverse_array(arr):
     return arr[::-1]
input_arr=[1,2,3,4,5]
output_arr=reverse_array(input_arr)
print("reversed array:", output_arr)
"""
# removing falsy values form an array(falsy= 0,False, none,[],(),{},"")
"""def removing_falsy_values(arr):
    result=[]
    for item in arr:
        if item:
            result.append(item)
    return result
input_arr= [1,2,False,0,"",[],8,{},763,"ddyw"]
output_arr=removing_falsy_values(input_arr)
print("only truthy values:",output_arr)
"""

# finding unique elements in the array
"""def unique_elements(arr):
    result=[]
    for item in arr:
        if arr.count(item)==1:
            result.append(item)
    return result
input_arr=[1,2,2,3,4,3,2,4,2,4]
output_arr=unique_elements(input_arr)
print("unique elements are:",output_arr)"""


"""a=10
b=20
a,b=b,a
print(a)
print(b)

a=10
b=20
c=0
c=a
a=b
b=c
print(a,b)"""

"""radius=int(input("enter the radius "))
area=3.14*radius*radius
circumference=2*3.14*radius
print(area,circumference)"""

"""celsius=int(input("enter celsius"))
fahrenheit=int(input("enter fahrenheit"))
fahrenheit=(9/5*celsius)+32
celsius=(fahrenheit-32)*5/9
print(fahrenheit)
print(celsius)"""

"""a=int(input("enter the num "))
if a%2==0:
    print("even")
else:
    print("odd")"""

"""a=int(input("enter the num "))
for i in range(1,a+1):
 b=a*a
print(b)"""

"""a=int(input("enter the year "))
if a%4==0 and a%100!=0 or a%400==0:
    print("it is a leap year")
else:
    print("normal year")"""

"""balance=200000
pin=input("enter your pin ")
if pin=="2404":
    print("correct balance is:",balance)
else:
    print("deny")
"""
"""fibo=1
for i in range(1,21):
    fibo*=i
    print(fibo)"""

"""num=int(input("enter a number"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)"""

"""n=int(input("enter a number"))
reverse=0
while n>0:
    i=n%10
    reverse=reverse*10+i
    n=n//10
print(reverse)
"""
"""n=int(input("enter a number"))
factorial=1
i=1
while i<=n:
      factorial*=i
      i=i+1
print(factorial)
"""

"""for i in range(1,21):
    if i%3==0:
        continue
    print(i)
"""

#Find first prime number greater than 50 using loop + break.
"""a=int(input("enter a number"))
if a>0:
    for i in range(2,a):
        if a%i==0:
            print("not prime")
            break
        else:
            print("prime")
else:
    print("not prime")"""

# Show use of pass inside an empty function.
"""def fnname():
    pass
fnname()"""

# Functions

# With parameters: Write a function that accepts a number and returns its factorial.
"""def fnmae(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)
fnmae(5)"""
# Without parameters: Function that prints “Hello, Python”.
"""def fnname():
    print(f"hello,python!")
fnname()
"""
# Return value: Function that accepts list of numbers and returns min, max, avg.
"""def fnname(n):
        minimum=min(n)
        maximum=max(n)
        avg=sum(n)/len(n)
        return minimum,maximum,avg
print(fnname([1,2,3,4,5]))"""

# Default parameters: Function greet(name, msg="Welcome!").
def default(name,msg="your msg"):
    print(f"{name}, {msg}")
default("name","welcome!")
# Positional arguments: Write function power(base, exp) → power(2, 5) = 32.
def power(base, exp):
    print(base**exp)
power(2,5)
# Keyword arguments: Call student(name="Varshini", age=20, course="Python").
def student(name, age, course):
    print(f"hello{name},age is {age}, im studying {course}")
student(course="python",name="jyothika",age=23)

# Variable length *args: Function that sums any number of arguments.
def vl(*nums):
    sum=0
    for i in nums:
        sum+=i
    print(sum)
vl(1,2,3,4)

# **kwargs: Function that handles student details (name, roll, course).
def sd(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}:{j}")
sd(name="jyo",age=23,course="python")

# Scoping (Local, Global, Nonlocal)

# Write program showing local variable shadowing a global variable.
"""var=10
def local():
    var=20
    print(var)
local()
print(var)"""

# Demonstrate global keyword by modifying global variable inside a function.
"""var=20
def glo():
    global var
    var+=10
    print(var)
glo()
print(var)"""

# Demonstrate nonlocal with nested functions.
"""def outfn():
    var=10
    def infn():
        nonlocal var
        var+=5
    print(var)
    infn()
    print(var)
outfn()
"""
# Problem solving: Accept password and check rules → must contain uppercase, digit, and special char.

#fibonacci series
"""num=int(input("enter how many fibonacci nums:"))
a,b=0,1
print("fibonacci sequence:")
for i in range(num):
    print(a,end="")
    a,b=b,a+b"""
"""
num=int(input("enter num:"))
count=0
for i in str(num):
    count+=1
print(count)"""

"""numbers=[1,2,3,4,4]
sum=0
for i in numbers:
    sum+=i
print(sum)"""

"""str=input("enter a string:")
if str==str[::-1]:
    print("palindrome")
else:
    print("not a plaindrome")"""

"""amt=19000
pin=int(input("enter pin:"))
if pin==2024:
    if amt==19000:
        withdraw=amt-1000
        print("you can withdraw money:",withdraw)
    else:
        deposit=1000+amt
        print("depositing 1000 rs to acc",deposit)
else:
    print("wrong pin")"""

"""n=int(input("enter a number:"))
if n>0:
    for i in range(2,n):
        if n%i==0:
          print("not prime")
          break
        else:
            print("prime")
else: 
       print("prime")"""
"""
for i in range(1,11):
    if i%2==0:
        print("even numbers",i)
    else:
        print("odd numbers",i)"""

"""str=input("enter a name:")
reverse=" "
for i in str:
    reverse=i+reverse
print(reverse)
"""

