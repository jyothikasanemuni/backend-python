# TASKS ON BREAK:
# 1.Find the first even numbers write a function that takes a list of integers and returns the first even number using a loop and break
def even_list(n):
    for i in n:
        if i%2==0:
           break
    return i
        
i=[1,2,3,4,5]
print("first even number is:",even_list(i))

#password validation: ask the user to enter a password .they get 3 tries .If the password is correct print"access granted" ,otherwise after 3 failed attempts .print "locked out".
for i in range(3):
    username=input("enter your username: ")
    password=input("enter your password: ")
    if (username=="admin") and (password=="password"):
        print("access granted")
        break
    else:
        print("wrong credentials, try again")
else:
    print("your acc is locked ")

# Infinite loop exit :write a true loop that keeps asking the input until the user types "exit",then stops using break
while True:
    user=input("enter your name: ")
    if user=="exit":
        print("your exited from the loop and stop")
        break
    else:
        print(f"hello {user} please enter again and again until you type exit!")


#TASKS ON CONTINUE
#Skip negative numbers : give a list  of integers and print only the positive ones using continue
numbers=[12,3,4,5,3.23,31,23,-2]
positives=[]
for i in numbers:
    if i<0:
        continue
    positives+=[i]
print("postives are:",positives)

#Skip vowels loop through a string and print only consonants using continue .example :"education".
string="education"
for i in string:
    if i in "aeiou":
        continue
    print("cosnants are:",i)

#Diivsible by 3 but not 5 :print all the numbers from 1-50 that are divisible by 3 but not divisible by 5
for i in range(1,51):
    if i%5==0:
        continue
    elif i%3==0:
        print("divisible by 3 but not 5:",i)

#TASKS ON PASS
#Define a placeholder fns : deine a fn process_data() thatsoes nothing for now.use pass
def process_data():
    pass

#Skeleton class :create a cls user with a pass block .you'll add functionality later
skeleton_class=[]
pass


#use pass in empty loop:create a loop ffrom 1-5 but do nothing inside the loop body
for i in range(1,6):
    pass

#MIXED CHALLENGES(USE BREAK,CONTINUE,PASS)
#Filter and stop :given a list of numbers ,print only those that are : even(use continue to skip odd numbers) less than 50(using break) -ignore 0(use pass if number is 0)
numbers=[1,2,34,4,50,642,7,70,8,95,10,0]
for i in numbers:
   if i==0:
      pass
      continue
   if i%2!=0:
      continue
   if i>50:
      break
   print("even",i)

#Word filter loop over a list of words: skip the words less than 3 characters stop if the word is "end" ,and do nothing (with pass) if the word is "wait". Example input:["hi","cat","dog","end","zebra"] Expected behaviour:-skips "hi" -prints "cat","dog"-ignores "wait" -stops at "end"
example=["hi","cat","dog","end","zebra"]
for i in example:
    if len(i)<=3:
        continue
    if i=="end":
        break
    if i=="wait":
        pass
print(i)