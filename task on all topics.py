#1. Variables
#1. Store your name in a variable and print a greeting message.
"""A="jyothika"
print(f"hello {A}!, have a good day")"""

#2. Store two numbers in variables and print their sum.
"""a=145
b=9324
print("The sum of numbers is:",a+b)"""

#3.Store the price of an item and quantity, then print the total cost.
"""quantity=5
price=95
Total_cost= quantity*price
print("the total cost is:",Total_cost)"""

#4. Store your age in a variable and print how many years are left until you turn 100.
"""age=23
years_left=100-age
print("years left until i turn 100 are:",years_left)"""

# 5. Swap the values of two variables without using a third variable.
"""a=20
b=35
a,b=b,a
print("The a's value is:",a)
print("The b's value is:",b)"""

#2. Data Types
#1. Create a list of three fruits and print the second one
"""fruits_list=["apple","banana","mango"]
print(fruits_list[1])"""

# 2. Store a sentence in a string and print its length
"""str="the datatypes are two types 10 primitive datatype these are immutuable and these contains int,float,str,bool,none and 20 non-primitive datatype these are mutuable and these contains list,tuple,set,dict."
print(len(str))"""

#3. Create a tuple of five integers and print the maximum number.
"""tuple=(1,4,6,23,456,3,1982,462,34)
print(max(tuple))"""

# 4. Create a dictionary with three student names as keys and their marks as values, then print the marks of one student.
"""dict={"ravi":64,"santosh":79,"praneeth":32}
print(dict["praneeth"])"""

# 5. Convert a string '123' into an integer and print its double.
"""str=int("123")
print(str*2)"""

# 3. Operators
#1. Take two numbers and print their sum, difference, product, and quotient.
"""a=67
b=23
print(f"The sum is:",(a+b),"the diff is:",(a-b),"the product is:",(a*b),"the quotient is:",(a/b))"""

#2. Take a number and check if it's even or odd using % operator.
"""num=94
if num%2==0:
    print("the number si even:",num)
else:
    print("the num is odd:",num)"""

# 3. Check if 'apple' is in the list ['banana', 'apple', 'mango'].
"""list= ['banana', 'apple', 'mango']
print("apple" in list)"""

# 4. Take a number and check if it's between 10 and 50 (inclusive).
"""num=int(input("enter a number"))
if 10<=num<=50:
    print("the number is b/w 10 and 50")
else:
    print("the number is not in b/w 10 and 50")"""

# 5. Find the remainder when 29 is divided by 5.
"""num=29
print("the remainder is:",num%5)"""

# 4. Conditional Statements
#1. Take a number and print 'Positive' if greater than zero, else 'Negative'.
"""num=int(input("enter a number:"))
if num>0:
    print("The num is positive")
else:
    print("The number is negative")"""

# 2. Take an age and print if the person is a child, teenager, or adult.
"""age=int(input("enter your age:"))
if age<13:
    print("you are a child")
elif 13<=age<=20:
    print("you are teenager")
elif 21<=age<=40:
    print("you are an adult")
else:
    print("you are old")"""

#3. Take three numbers and print the largest one.
"""numbers=[122323,173342,868348]
largest_num=0
for i in numbers:
        if i > largest_num:
            largest_num = i
print("the largest number is:",largest_num)"""

#4. Check if a given year is a leap year or not.
"""year=int(input("enter no.of days in a year:"))
if year==363:
    print("The year is leap year")
else:
    print("the year is not a leap year")"""

# leap year
"""year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")"""

# 5. Take a mark and print 'Pass' if it is 40 or more, otherwise 'Fail'.
"""marks=int(input("enter your marks:"))
if marks>=40:
    print("pass")
else:
    print("fail")"""

#5. Control Statements
#1. Print numbers from 1 to 10, but skip the number 5 using continue.
"""for i in range(1,11):
    if i==5:
        continue
    print(i)"""

#2. Print numbers from 1 to 20, but stop when you reach 13 using break.
"""for i in range(1,21):
    if i==13:
        break
    print(i)"""

# 3. Print all even numbers from 1 to 10, skipping odd numbers.
"""for i in range(1,11):
    if i%2!=0:
        continue
    print(i)"""

# 4. Use a loop to print numbers from 1 to 5, but use pass inside the loop body.
"""for i in range(1,6):
    pass
    print(i)"""

# 5. Continuously take input from the user until they type 'exit'.
"""while True:
 num=input("entera number")
 if num=="exit":
  print("stop the loop")
  break
print(num)"""

#6. Loops
#1. Print numbers from 1 to 10 using a for loop.
"""for i in range(1,11):
    print(i)"""

# 2. Print numbers from 10 to 1 using a while loop.
"""i=10
while i>=1:
    print(i)
    i=i-1"""

# 3. Print the sum of numbers from 1 to 100.
"""sum=0
for i in range(1,101):
    sum=sum+i
print(sum)  """

# 4. Print all elements of a list using a loop.
"""list=[1,2,3,3,21]
for i in list:
    print(i)
"""
# 5. Take a number n and print its multiplication table from 1 to 10.
"""num=int(input("entera num:"))
for i in range(1,11):
    print(num ,'x', i, '=', num*i)"""

#7. User-Defined Functions
#1. Write a function that takes a name and prints 'Hello, <name>!'.
"""def taking(name):
    print(f'hello,{name}!')
taking("jyothika")"""

#2. Write a function that takes two numbers and returns their sum.
"""def sum(a,b):
    return a+b
print(sum(3,4))"""

# 3. Write a function that checks if a number is even or odd.
"""def even_odd(num):
    if num %2==0:
        return "even"
    else:
        return "odd"
print(even_odd(5))"""

#4. Write a function that takes a list of numbers and returns the largest one.
"""def numbers(num):
    largest=0
    for i in num:
        if i > largest:
            largest=i
    return largest

nums=[1,33,423422,14]
print("the largest num is:",numbers(nums))"""

# 5. Write a function that takes a number and returns its factorial.
"""def factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    return factorial
print(factorial(9))
"""

