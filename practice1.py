"""# Take marks as input and categorize: Distinction, First Class, Second Class, Fail.
marks= int(input("enter a number:"))
if marks>=85:
    print("distinction")
elif marks>=65:
    print("first cls")
else:
    print("fail")

# Accept three sides of a triangle and check if it is equilateral, isosceles, or scalene.
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if a==b==c:
    print("that is equilateral")
elif a==b or b==c or c==a:
    print("isosceles")
else:
    print("scalene")


# Check if a number is divisible by both 3 and 5 but not 15.
x=int(input("enter a number:"))
if x%3==0 and x%5==0:
    print("divisible by both")
elif x%3==0:
    print("divisible 3")
elif x%5==0:
    print("divisible 5")
else:
    print("other number")"""

# Looping Statements
# Print the first 20 Fibonacci numbers using a for loop.
"""n = int(input("Enter how many Fibonacci numbers: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b"""
# Generate all prime numbers from 1–200 using a while loop.


"""# Create a multiplication table (1–10) using nested loops.
num=int(input("enter a number"))
for i in range(1,11):
    print(num ,'x', i, '=',num*i )"""

# Write a program that prints numbers from 1–50 but skips numbers divisible by 7.
"""for i in range(0,51):
    if i%7==0:
        continue
    print(i)
"""
# Search for a number in a list; break loop when found and display index.
"""list=[12,1,3,5,3,2]
for i in list:
    if i==5:
          break
    print(i)
print("the index number is:",list.index(i))
"""
# Use nested loops with break to stop execution when sum of row elements exceeds 50.


# Functions (parameters)

"""# Write a function that takes name and age (positional args) and prints them.
def funcname(name,age):
     print(f"welcome {name} and my age is {age}")
funcname("jyothi",23)
    
# Create a function with default parameters to calculate area of rectangle (default length=5, breadth=3).
def areaofrectangle(length,breadth):
     print("the area of rectangle:",length*breadth)
areaofrectangle(5,3)

# Implement a function that accepts any number of positional arguments and returns their sum.
def fn(*nums):
    total=0
    for i in nums:
        total+=i
    return total
print("the sum of numbers:",fn(3,4,5))

# Implement a function that accepts keyword arguments for student details and prints them neatly.
def studentdetails(name,id,add,phno):
     print(f" welcome {name} ur id no is {id} ur address is {add} and ur contact is {phno}")
studentdetails(name="jyothika" , phno=6342834, id=213234,add="bollaram")

# Write a function with both *args and **kwargs to handle course registrations.
def func(*courses, **studentdetails):
    for i in courses:
          print(f"welcome to",i)
    for i,j in studentdetails.items():
         print(f"{i}:{j}")
func("python","java",name="jyothika",age=23,add="bollaram")
         

# Functions (return values)

# Write a function that returns factorial of a number.
def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
print("the factorial of a number is:",factorial(5))

# Create a function that returns multiple values (min, max, average) of a list.
def multiple(nums):
     maximum=max(nums)
     minimum=min(nums)
     average= sum(nums)/len(nums)
     return minimum ,maximum ,average
print(multiple([1,2,3,4,5]))
"""
# Implement a recursive function that reverses a string.

#  Scoping

# Write a program demonstrating modification of a global variable inside a function.
"""var=20
def glovar():
    global var
    var+=5
    print(var)
glovar()
print(var)"""

# Write nested functions where the inner function modifies a variable using nonlocal.
"""def outfn():
    var=30
    def infn():
        nonlocal var
        var+=5
        print(var)
    infn()
outfn()"""


# Show example where local variable shadows a global variable.
"""var=20
def fn():
    var=10
    print(var)
fn()
print(var)"""

#Check if a string is palindrome
"""str="jyothika"
if str==str[::-1]:
        print("palindrome")
else:
        print("not palindrome")"""

"""num=int(input("entera number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)
"""
"""for i in range(1,11):
    print(i**2)
"""
