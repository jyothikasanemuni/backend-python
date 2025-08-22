# task 1 swapping two numbers by using temp
"""a=5
b=6
Temp=0

temp=a
a=b
b=temp
print(a)
print(b)"""

#task2 :identify data operators :- input three values from the user and print their values
"""a=eval(input("enter a value:"))
b=eval(input("enter b's value:"))
c=eval(input("enter c's value:"))
print(type(a))
print(type(b))
print(type(c))
"""
#task 3: simple calculator:  perform +,-,*,/,//,%,** on two numbers based on the user input.
"""a=int(input("enter a's value:"))
b=int(input("enter b's value:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)"""

#task 4: salary hike:- take salary and apply 15% hike .print odd and new salary

"""salary=int(input("enter the salary:"))
salary_with_hike= salary* 0.15
newsalary= salary + salary_with_hike
print("salary_with_hike is:",salary_with_hike)
print("new salary is:",newsalary)
"""
#task 5: area and perimeter of circle :- use radius to calculate area and perimeter 

"""radius=int(input("enter the radius:"))
area= 3.14 * radius * radius
perimeter= 2 * 3.14 * radius
print("The area of a circle is:",area)
print("The perimeter of a circle is:", perimeter)"""

#task 6: ASCII character :- input a character and print the acsii using ord().
"""
ASCII=input('enter a character:')
print("the value of ASCII IS:",ord(ASCII))"""

#Task 7: check even or odd :-use modulus operator to determine if a number is even or odd
"""a=int(input("enter a number:"))
if a %2==0:
    print("even")
else:
    print("odd")"""

#task 8: compound assignment practice: use +=,-=,*=,/=,%=,//=,**= opeartor on a variable.show result after each
"""
a=5
a+=3
print(a)

b=7
b-=2
print(b)

c=6
c*=2
print(c)

d=19
d/=5
print(d)

e=34
e%=2
print(e)

f=83
f//=3
print(f)

g=9
g**=2
print(g)"""

#task 9: boolean and logical check:- use logical operators to check age and name validity.

"""name="jyothika"
age=23
if name and age>=18:
    print("valid")
else:
    print("invalid")
"""

#task 10:- bitwise shift practice :-perform left shift and right shift by 1 and 2 .explain changes mathematically

"""a=6
print(a<<2) # 6 << 2 = (by bits values if we shift 2bits to left) 16+8=24

b=7
print(b>>1) # 7 >> 1 = (by bits values if we shift 1 bit to right side) 2+1=3
"""

#task 11: bitwise AND,OR,XOR,NOT:- use a =12,b=5 to demonstrate &,|,^,~ operators

"""a=12 #1100
b=5  #0101
print(a & b) 
print(a|b)
print(a^b)
print(~a)
print(~b)"""

#task 12: datatype conversion: convert str to int ,float to str,int to bool.print result and type

"""a="12341"
b=int(a)
print(type(b),b)

b=3.13123
c=str(b)
print(type(c),c)

c=90
d=bool(c)
print(type(d),d)"""

#task 13: Temperature conversion: convert celsius to fahrenheit and vice versa
#task 14: quotient and remainder: use/ and % to get quotient and remainder.check divisiblity.
"""
a=int(input("enter a's num:"))
b=int(input("enter b's num:"))
quotient = a//b
remainder=a%b
print("remainder:",remainder) #remainder
print("quotient",quotient) # floor division

if remainder==0:
    print("divisible")
else:
    print("not divisible")"""

#task 15: string opeartions: use string methods: upper(),lower(),len() and "in"

"""str="JyOTHika SanEmuni"
print(str.upper())
print(str.lower())
print(len(str))
print("i" in str)
"""
# task 16: sum of digits:  input 3 digit numbera nd sumdigits using // and % only.

"""num=int(input("enter 3 digit num:"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum of ndigits:",sum)"""

#task 17: identity vs equality: use== and is with two list to compare
"""
a=[1,2,3]
b=[1,2,3]
print(a==b)
b=a
print(b is a)"""

#task 18: Age in months and Days: convertage in years to months and days
"""age_years = int(input("Enter your age in years: "))
age_months = age_years * 12
age_days = age_years * 365 
print("Age in months:", age_months)
print("Age in days:", age_days)"""

#task 19:type guessing: analyze type of x=10+3.5,y="age:"+str(30),z=true+false+2
"""x=10+3.5
print(type(x))
y="age:"+str(30)
print(type(y))
z=True+False+2
print(type(z))"""
#task 20:bitwise practice(no bin()): use a number n and show ~n,n<<1,n>>2. explain mathematically
"""print(~5) #~n= -(n+1)
print(7>>1)  # 7 >> 1 = (by bits values if we shift 1 bit to right side) 2+1=3
print(6<<2)  # 6 << 2 = (by bits values if we shift 2bits to left) 16+8=24"""

