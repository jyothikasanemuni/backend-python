# break using for loop
"""list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)
    if i==5:
        break"""

#break using while loop
"""i=0
while True:
    print(i)
    if i == 100:
        break
    i+=1"""

#continue using for loop
"""list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i ==6:
        continue
    print(i)
   """
# continue using while loop
"""i=0
while (i<=20):
    i=i+1
    if i==6:
        continue
    print(i)"""

# continue using for loop
"""for i in range(20):
    if i==6:
        continue
    print(i)"""
    
#pass using while
"""i=0
while i<10:
    i=i+1
    if i ==5:
        pass
    print(i)"""

#pass using for 
"""for i in range(10):
    if i==5:
        pass
    print(i)
    """

#using for loop take a range from 1 to 100 and print numbers, if the numbers is divisible 

"""
for i in range(1,101):
    if i % 57==0:
        print("current number is divisible by 57:",i)
        break
    print(i)
"""

"""
while True:
    string=input("enter a value(enter 'quit' or 'exit')to exit the loop:" )
    if string.lower()=='quit' or string.lower()=='exit':
        print("have a nice day")
        break
    print(string)"""
#using while loop take a string if we get exit or quit we have to print "have a nice day"
"""while True:
    string=input("enter a value(enter 'quit' or 'exit')to exit the loop:" )
    if string.lower() in ['exit','quit','done']:
        print("have a nice day")
        break
    print(string)"""


#skip all teh even numbers in a given range from 1 to 50 using continue
"""
for i in range(1,51):
    if i%2==0:
        continue
    print(i)"""

#skip all the vowels in a given string using continue (ex:education o/p:dcton)
"""string=input("enter a string: ")
vowels="aeiou"
for i in string:
    if i.lower() in vowels:
        continue
    print(i,end="")
"""
#OR

"""string=input("enter a name: ")
for i in string:
    if i=="a" or i=="e" or i=="i" or i=="o"  or i=="u":
        continue
    print(i)"""