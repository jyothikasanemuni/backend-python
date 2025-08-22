#print all the numbers from 1 to 50, but skip numbers divisible by 3 using continue
"""for i in range(1,51):
    if i%3==0:
        continue
    print(i)"""

# Keep asking the user to enter numbers. When a number is divisible by 11 is entered, print a message and exit the loop using break.
"""while True:
 num=int(input("Enter a number:"))
 if num%11==0:
        print("yeah! the entered number is divisible by 11,exiting the loop")
        break
      """

# multiplication table
"""num=int(input("entera number:"))
for i in range(1,11):
    print(num, "x",i,"=",i*num)"""

#
"""str=input("enter a name:")
count=0
for i in str:
    if i in "aeiou":
        count=count+1
print(count)
"""
"""while True:
    pas=input("password:")
    if pas =="admin123":
        break
    print(pas)"""

"""for i in range(1,11):
    user=int(input("enter 10 no:"))
    if user<0:
        continue
    print("postive numbers",user)"""


#password validation
"""for i in range(1,4):
    user= input("password:")
    if user=="admin123":
        print("acces granted")
        break
else:
     print("locked out")"""

"""while True:
    user=input("enter a string:")
    if user=="exit":
        break
"""
"""ls=[1,2,3,4,-9,-3,-5]
for i in ls:
 if i < 0:
   continue
 else:
    print("positives:",i)"""

"""for i in range(1,51):
    if i%5!=0:
        continue
    elif i%3==0:
        print("numbers",i)"""

#pass 
"""
def process_data():
    pass
process_data()"""

"""for i in range(1,6):
    pass
"""


# Keep asking the user to enter numbers. When a number is divisible by level is entered, print a message and exit the loop using break.
while True:
    user=int(input("enter a number:"))
