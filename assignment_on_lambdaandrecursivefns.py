# Lambda Functions
# Beginner
#  • Write a lambda function to check if a number is even or odd.
even_odd=lambda x: "even" if x%2==0 else "odd"
print(even_odd(4))
#  • Write a lambda function to find the maximum of two numbers.
max=lambda a,b: a if a>b else a<b
print(max(5,4))
#  • Write a lambda function to compute the square of a number.
square=lambda x: x**2
print(square(9))

# Intermediate
#  • Use map() with a lambda to convert a list of Celsius temperatures to Fahrenheit.
celsius=[21,32,45,76,89]
fahrenheit=list(map(lambda x:(x*9/5)+32,celsius))
print(fahrenheit)
#  • Use filter() with a lambda to extract even numbers from a list.
list1=[1,2,3,4,5,6,7,8,10]
evens=list(filter(lambda x:x%2==0,list1))
print(evens)
#  • Use reduce() with a lambda to calculate the product of all numbers in a list.
from functools import reduce
list2=[1,2,3,4,5,6,7,8]
products=reduce(lambda x,y:x*y,list2)
print(products)
#  • Use sorted() with a lambda to sort a list of tuples by the second element
numbers = [(1, 7), (3, 9), (5, 6)]
sorting=sorted(numbers,key=lambda x:x[1])#second elements i list of tuples are 7,9,6---> 6,7,9
print(sorting)

# Recursive Functions
# Beginner
#  • Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
#  • Write a recursive function to calculate the sum of first N natural numbers.
def sum_n(num):
    if num==0:
        return 0
    else:
        return num+sum_n(num-1)
print(sum_n(9))
#  • Write a recursive function to reverse a string.
def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]
print(reverse("jyothika"))
# Intermediate
#  • Write a recursive function to find the Nth Fibonacci number.
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=7
for i in range(n):
    print(fibonacci(i),end="")
#  • Write a recursive function to calculate the sum of digits of a number.
def sum_of_digits(num):
    if num==0:
        return 0
    else:
        return (num%10)+sum_of_digits(num//10)
print(sum_of_digits(12345))
#  • Write a recursive function to check if a string is a palindrome.
#  • Write a recursive function to calculate the power of a number (x^n).
def power_n(x,y):
    if y==0:
        return 1
    else:
        return x*power_n(x,y-1)
print(power_n(3,4))
