#functions 
#TASKS ON RETURN vALUES
#write a function that returns the cube of a numbers
def cube(n):
    return n**3
print("the cube of the value is :",cube(5))

#Write a fn that takes two numbers and returns their avg
def avg(a,b):
    return (a+b)/2
print("the avg of the values",avg(3,4))

#write a fn  that returns both the squares and squareroot of a number
def squares(n):
    return n**2 , n**0.5
print("the square and squarerrot of num is:",squares(36))

#create a fn is_odd(n) that returns True if the number is odd,else False
def is_odd(n):
    return n%2!=0

print(is_odd(4))

#Write a fn sum_of_digits(n) that returns the sum of digits of a number.(ex:- sum_digits(1234) should return 10)
def sum_of_digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum
print(sum_of_digits(1234))

#TASKS ON FUNCTIONS WITH DEFAULT PARAMETERS
#create a fn greet(name="guest")thet returns "Hello,!".
def greet(name="guest"):
    return f"hello,!"
print(greet())

#create a fn power(base,exponent=2) that returns base**exponent.
def power(base,exponent=2):
    return base ** exponent
print(power(2))

#create a fn total_bill(item="sandwich",quantity=1,price=50) that returns total price
def total_bill(item="sandwich",quantity=1,price=50):
    return quantity*price
print(total_bill("burger",3,100))

#create a fn employee_info(name,age=30,dept="hr")thet returns a formatted string
def employee_info(name,age=30,dept="hr"):
    print(f"hi! this is {name} and my age is {age} , i'm from {dept} department")
employee_info("jyothika",22)

#create a fn circle_area(radius=1) that returns the area of a circle(area=3.14*radius*radius)
def circle_area(radius=1):
    return 3.14*radius*radius
print("the area of the circle is:",circle_area(4))

#TASKS ON LOOPS WITH RETURN
#Write a fn that takes a number and return the sum of all even numbers upto that number
def even(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum=sum+i
    return sum
print(even(50))

#write a fn that returns the largest number from a list of numbers passed as a parameter
def list_of_numbers(n):
    largest=0
    for i in n:
        i>largest
        largest=i
    return largest
list=[1,2,3,4,5,6,7,8,9]
print("the largest num is: ",list_of_numbers(list))


#TASKS WITH MULTIPLE RETURN VALUES
#Create a fn min_max(nums) that returns the minimum and maximum values in a list
def min_max(nums):
    minimum=min(nums)
    maximum=max(nums)
    return minimum,maximum
numbers=[12,23,34,45,56,67,78,89]
print("the minimum and maximum from the list are :",min_max(numbers))

#create a fn student_summary(name,marks) that returns the student's name, total marks,and average marks
def student_summary(name,a,b):
    return name,(a+b), (a+b)/2
print(student_summary("jyo",23,56))

#LOGICAL TASK
#Create a fn calculate (num1,num2,operator="+") that does :-return sum, return difference,return product,return quotient .use return and default parametets for operator
def calculate(num1,num2,operator="your choice"):
    if operator=="+":
        return (num1+num2)
    elif operator=="-":
        return (num1-num2)
    elif operator=="*":
        return (num1*num2)
    elif operator =="/":
        return (num1/num2)
    else:
        return "inaalid operator"
print(calculate(2, 9, "+"))  
print(calculate(-7, 2, "-"))  
print(calculate(5, 8, "*"))  
print(calculate(8, 9, "/")) 

