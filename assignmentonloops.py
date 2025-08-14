#Print Numbers Except Multiples of 3
#Print all numbers from 1 to 50, but skip numbers divisible by 3 using continue.
for i in range(1,51):
    if i%3==0:
        continue
    print(i)

#First Multiple of 11
#Keep asking the user to enter numbers. When a number divisible by 11 is entered, print a message and exit the loop using break.
while True:
 num=int(input("Enter a number:"))
 if num%11==0:
        print("yeah! the entered number is divisible by 11,exiting the loop")
        break

#Count Vowels in a String
#Take a string input from the user and count how many vowels (a, e, i, o, u) it contains.
str=input("enter your name:")
count=0
for i in str:
    if i.lower() in'aeiou':
        count+=1
print(count)

#Reverse Even Numbers
#Print all even numbers from 100 to 2 in reverse using a while loop.
i=100
while i>=2:
    if i%2==0:
        print(i)
    i=i-1

#Password Verification
#Ask the user to enter a password repeatedly until they type "admin123". Use a while loop and break.
while True:
    password=input("password:")
    if password =="admin123":
        break
    print(password)

#Multiplication Table (1–10)
#Take a number from the user and print its multiplication table from 1 to 10 using a for loop.
num=int(input("enter a num:"))
for i in range(1,11):
    print(num,'x',i,'=',num*i)

#Skip Negative Numbers
#Ask the user to input 10 numbers. Skip negative numbers using continue and print only the positive ones.
for i in range(1,11):
    user=int(input("enter 10 num's:"))
    if user<0:
        continue
    print(user)
 
#Sum of N Odd Numbers
#Ask the user to enter a number N. Find and print the sum of the first N odd numbers using a loop.
n = int(input("Enter N: "))
total = 0
for i in range(1, n * 2, 2):
    total += i
print(total)


#List Prime Numbers from 1 to 50
#Using a loop and continue, print all prime numbers between 1 and 50.
for i in range(1,51):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

#Running Total Until Zero
#Ask the user to keep entering numbers. Keep a running total and stop when the user enters 0. Then print the total sum.
total=0
while True:
    num=int(input("kepp entering the numbers until you enter 0:"))
    if num==0:
        break
    total+=num
print(total)
    




