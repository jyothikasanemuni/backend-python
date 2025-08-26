

#print numbers from 1 to 5 using a while loop
i=1
while i<=5:
    print(i)
    i+=1

#print even nums from 1-10 using while
i=1
while i<=10:
    if i%2==0:
     print(i)
    i=i+1

#sum of numbers 1-10 using while
n=int(input("enter a num:"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)

#print each digit of a number using while (ex: i/p:123  o/p:1 2 3)
i=1
while i<=3:
    print(i,end="")
    i=i+1
# #or
num=input("enter a num: ")
i=1
while i <=len(num):
    print(i,end=" ")
    i=i+1

# print numbers from 10-1 using while loop
i=10
while i>=1:
    print(i)
    i=i-1

#FOR LOOP
#print numbers from 1-10 using for loop
for i in range(1,11):
    print(i)

#print each character in the word banana using for loop
n="banana"
for i in n:
    print(i)

#print squares of numbers fromm 1-5 using for loop
for i in range(1,6):
    print(i**2)

#print all even numbers in the list
list=[]
for i in range(1,11):
    if i%2==0:
     list.append(i)
print(list)

#print numbers form 1-20 that are divisible by 3 using a for loop
for i in range(1,21):
   if i%3==0:
      print(i)

#star pattern
i=3
for i in range(1,i+1):
    print("*"*i)

#numbers pattern
for i in range(3): #rows 
    for j in range(1,4): #columns
        print(j,end="")  #print j on same line
    print()   #go to next line after finishing a row

#number star pattern
for i in range(1,4):  
    for j in range(1,i+1):
        print(j,end='')
    print()

#print multiplication table
n=int(input("enter a number: "))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

#print each character of two words in a list using nested loop words=["hi","ok"]

# SECTION 4: Loops with conditions(No break/continue)
#print numbers from 1 to 10 and print "even" or "odd" next to each.
for i in range(1,11):
    if i%2==0:
      print("even",i)
    else:
       print("odd",i)
      
#ask the user to enter 5 numbers and print only the even numbers
for i in range(5):
    num=int(input("enter a num: "))
    if num%2==0:
      print("even number:" ,num)

#ask user to enter numbers until they enter a negative number and then stop.
n=0
while n>=0:
    n=int(input("enter a number: "))
if n>=0:
    print("you entered number:")
else:
    print("you entered negative number so loop stopped")

#print vowels in a word using a for loop and if condition
str=input("enter the string: ")
list=[]
for i in str:
    if i in "aeiou":
        list.append(i)
print(list)

#count how many vowels aare in a given word
str=input("enter the string: ")
count=0
for i in str:
    if i in "aeiou":
        count+=1
print(count)

# SECTION 5:CREATIVE AN FUN LOOP TASKS
#print the word "hello" 5 times using a loop
for i in range(1,6):
    print(i,"hello")

#ask the user their fav color 3 times using a loop
for i in range(4):
    print(input("enter your fav color: "))

#print pattern using nested loop 
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
for i in range(3):   # 3 rows
    print(letters[i] * (i+1))

#count how many times the letter a apperas in "banana"
str="banana"
count=0
for i in str:
    if i=="a":
        count+=1
print(count)

#print numbers from 1-10. for each ,print "small" is it's<5 ,else print "big"
for i in range(1,11):
    if i<5:
        print("Small",i)
    else:
        print("Big",i)