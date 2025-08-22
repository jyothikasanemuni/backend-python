#function by prameters
"""def arithmetic_operator(a,b):
    print((a+b),(a-b),(a*b),(a/b))
arithmetic_operator(5,6)"""

#using function concatenation and replication of strings with parameters
"""def string(str1,str2,num):
    print((str1+str2),(str1*num))
string("jyo","hima",4)"""

# write a function to print n numbers
"""def numbers():
    num=int(input("enter a number:"))
    for i in range(0,num):
        print(i)
numbers()
"""
#relicating the string with list,tuple,set and dictionary
"""
list=["hi","jyo","hima"]
list1=['1','f','r']
list2=3
print(list+list1)
print(list*list2)
"""
"""tuple1=('a','b','c')
tuple2=('d','e','f')
print(tuple1+tuple2)
"""

"""tuple=(1,2,3,4)
set={1,4,5}
dictionary={'name':'jyo','contact':234567}"""

# function using return
"""def sub(a,b):
    return a-b
print(sub(20,30)-10, sub(10,30)*3, sub(20,90)/4, sub(65,30)**2)"""

#task 2: write a function that takes a list as input and find out all the even num's in a list and return sum.
"""def sum_of_even(num):
    sum=0
    for i in num:
        if i%2==0:
            sum=sum+i
    return sum
list=[1,2,3,4,5,6,7,8,9,10]
print("sum of even num's is:",sum_of_even(list))"""

#cube of a number 
"""def cube_of_num(a):
    return a**3
print(cube_of_num(5))"""

#write a function that takes two values and return the average
"""def avg_of_2_num(a,b):
    return (a+b)/2
print(avg_of_2_num(10,20))"""

#write a function that returns both the squares and squareroot of the number.
"""def squares_and_squareroot(a):
    return a**2, a**0.5
print(squares_and_squareroot(5))"""

#create a function is_odd(n) that returns True is the num is odd ,else False.
"""def is_odd(n):
    if n%2 !=0:
        return "True"
    else:
        return "False"
print(is_odd(3))
"""
# write a function for sum of digits
"""def sum_of_digits(num):
    sum=0
    for i in str(num):
        sum=sum+int(i)
    return sum
print(sum_of_digits(1234))"""

# no 1 task in default parameters
"""def greetings(name="Guest"):
    return "hello,!"
print(greetings())"""

# no 2 task in default parameters
"""def power(base,exponent=2):
    return base ** exponent
print(power(4))
"""
#no 3 task in default parameters
"""def total_bill(item='sandwich', quantity=1, price=50):
    return quantity*price
print(total_bill())"""

#no 4 task in default parameters
"""def employee_info(name, age=30,department='HR'):
    return(f"Hi this is {name}, my age is {age},from {department} department")
print(employee_info("jyo"))"""

#no 4 task in default parameters
"""def circle_area(radius=1):
    return 3.14*radius*radius
print("Area of the circle is:",circle_area())"""

# no 1 task in loops with return
"""def sum_of_even(num):
    sum=0
    for i in str(num):
        if int(i) %2==0:
            sum=sum+int(i)
    return sum
print(sum_of_even(1234578))"""

# no 2 task in loops with return


#
"""def student_summary(name,marks):
    return(f"{name}", {marks}, a+b)"""


#keyword arguments
"""def personal_details(name,fathername,mothername,college,btechcourse,siblings,phno):
    print(f"hello{name},my father name is: {fathername} my mother name is: {mothername} recently graduated from {college} in {btechcourse} and coming to my siblings her name is {siblings} and my contact info is:{phno}")
personal_details(fathername="yadagiri",phno=23642834,siblings="moulika",btechcourse="CSE",college="Ellenki",mothername="prasanna", name="jyothika")"""

"""
def number(*num):
    mul=1
    for i in num:
        mul*=i
    return mul
print(number(1,2,3,3,4,4,3,4))"""

"""def details(*urdetails):
    for i in urdetails:
        print(i)
details("senu",23,3452834)"""

"""def details(**urdetails):
    for i,j in urdetails.items():
        print(f'{i}:{j}')
details(name="jyo", age=23, phno=23564182)"""
"""
def details(urdetails):
    for i,j in urdetails:
        print(f'{i}:{j}')
values={"age":23,"name":"jyo"}
print(values) """

"""def operations(a,b):
    return a%b,a//b
remainder,quotient=operations(3,45)
print(remainder)
print(quotient)
"""
  


#1. FUNCTIONS WITHOUT PARAMETERS & WITHOUT RETURN VALUE
# 1. Print numbers 1 to 10
"""def function():
    for i in range(1,11):
        print(i)
function()"""

# 2. Check even numbers between 1 and 20
"""def even_num():
    for i in range(1,21):
        if i%2==0:
            print(i)
even_num()"""

# 3. Print multiplication table of 5
"""def mul_table(num):
    for i in range(1,11):
        print(num,"x",i,"=",i*num)
mul_table(5)"""

 # 4. Print all odd numbers from 1 to 15
"""def odd_num():
    for i in range(1,16):
        if i%2!=0:
            print(i)
odd_num()"""

# 5. Print countdown from 10
"""def countdown():
    for i in range(10,1,-1):
       print(i)
countdown()"""

# FUNCTIONS WITHOUT PARAMETERS BUT WITH RETURN VALU
# 1. Return sum of numbers 1 to 10
"""def sum_of_num():
    sum=0
    for i in range(1,11):
        sum=sum+i
    return sum
print(sum_of_num())"""

 # 2. Return largest number in range 1-50 divisible by 7
"""def largest_num():
    largest=0
    for i in range(1,51):
        if i%7==0:
            largest=i
    print(largest)
largest_num()"""
# 3. Return count of even numbers in range 1-30
"""def count_even_num():
    count=0
    for i in range(1,31):
        if i%2==0:
            count+=i
    return count
print(count_even_num())"""

 # 4. Return factorial of 5
"""def factorial_num(num):
    factorial=1
    for i in range(1,6):
        factorial*=i
    return factorial
print(factorial_num(5))"""

 # 5. Return list of numbers divisible by both 3 and 5 from 1-50
"""def divisibility():
    result=[]
    for i in range(1,51):
        if i%3==0 and i%5==0:
           result.append(i)
    return result
print(divisibility())
"""
#3. FUNCTIONS WITH PARAMETERS & WITHOUT RETURN VALUE
# 1. Print numbers up to n
"""def numbers(num):
    for i in range(1,num+1):
        print(i)
numbers(12)"""

# 2. Print multiplication table of given number
"""def mul_table(num):
    for i in range(1,11):
        print(num,"x",i,"=",i*num)
mul_table(12)"""

 # 3. Print even numbers up to n
"""def even_num(nums):
    for i in range(1,nums+1):
        if i%2==0:
            print(i)
even_num(100)"""

# 4. Print factorial of given number
"""def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
factorial(8)"""

# 5. Print reverse from n to 1
"""def reverse(num):
    for i in range(num,0,-1):
        print(i)
reverse(12)"""

#4. FUNCTIONS WITH PARAMETERS & WITH RETURN VALUE
# 1. Return sum of numbers up to n
"""def sum_of_num(nums):
    sum=0
    for i in range(1,nums+1):
        sum+=i
    return sum
print(sum_of_num(25))"""

# 2. Return number of even numbers up to n
"""def even_num(nums):
    evens=0
    for i in range(1,nums+1):
        if i %2==0:
            evens=evens+1
    return evens
print(even_num(30))"""

 # 3. Return factorial of n
"""def factorial(nums):
    factorial=1
    for i in range(1,nums+1):
        factorial*=i
    return factorial
print(factorial(9))"""

# 4. Return list of odd numbers up to n
"""def odds(nums):
    result=[]
    for i in range(1,nums+1):
        if i%2!=0:
            reslut=result.append(i)
    return result
print(odds(30))"""

 # 5. Return largest number in given range divisible by k
"""def divisible_by_k(num,k):
    largest=0
    for i in range(1,num+1):
        if i%k==0:
            largest=i
    return largest
print(divisible_by_k(45,6))"""

#5. POSITIONAL ARGUMENTS
# 1. Print multiplication of two numbers
"""def mul_of_2(a,b):
   print(a*b)
mul_of_2(2,5)
"""
 # 2. Print numbers from start to end
"""def start_end(start,end):
    for i in range(start,end+1):
        print(i)
start_end(1,9)"""

# 3. Print all even numbers between two numbers
"""def even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
even(2,20)"""

# 4. Print table of number up to limit
"""def mul_table(num,limit):
    for i in range(1,limit+1):
        print(f"{num} x {i} ={num*i}")
mul_table(8,5)"""

# 5. Print sum of range
"""def sum(m,n):
    sum=0
    for i in range(m,n+1):
        sum+=i
    print(sum)
sum(2,18)"""















