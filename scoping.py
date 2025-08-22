"""def local():
    x=10
    print(x)
local()"""
#print(x) this shows the error :-NameError: name 'x' is not defined

# 1 Write a function `display_message()` that defines a local variable `msg` and prints it. Try printing `msg` outside the function and observe what happens.

"""def display_msg():
    x="msg"
    print(x)
display_msg()"""
#print(x) this shows the error :-NameError: name 'x' is not defined

#2 Create a function `add_numbers()` that takes two numbers, stores their sum in a local variable, and prints the sum. Confirm that the local variable is not accessible outside the function.
"""def add_numbers():
    a=12
    b=98
    print(a+b)
add_numbers()"""
#print(a+b)  this gives an error, so this can't be accesed outside the function

#GLOBAL VARIABLES
"""a=92
def glovar():#global variable
    print(a)
glovar()
print(a)"""#this doesn't give an error bcoz this is global variable so the var is accesed outside the function too..

# 1 Create a global variable `counter` and initialize it to `0`. Write a function `increase_counter()`that does not use the `global` keyword but tries to increment the counter. Run it and see what happens.
"""counter =0
def increase_counter():
    counter=0 ## This creates a local variable
    counter+=1 # Increments the local variable 
    print(counter) # Prints the local counter 1
increase_counter()
print(counter) # this print the global variable 0"""

# 2 Rewrite `increase_counter()` using the `global` keyword so that it successfully modifies the global `counter`.
"""counter=0
def increase_counter():
    global counter # using the global keyword
    counter+=1     #increments global variable
    print(counter) #print the global value
increase_counter()
print(counter)     #gives output as 1 bcoz we used global keyword."""

# 3 Create a global list `students`. Write a function `add_student(name)` that appends a name to the global list without redeclaring it.
"""students=[]       # global list
def add_student(name):
    students.append(name) #appends a name to the global list
add_student("jyo")
print(students)"""

# NONLOCAL/ENCLOSING VARIABLE SCOPE
"""def outerfunc():
    var=24
    def innerfunc():
        print(var)
    innerfunc()
outerfunc()
#print(var) # this gives the error:- NameError: name 'var' is not defined."""

#1 Create a nested function where the outer function defines a variable `language = "Python"`. The inner function should print that variable.
"""def outerfunc():
    language='python'
    def innerfunc():
        print(language)
    innerfunc()
outerfunc()"""

#2 Modify the above task so that the inner function changes the value of `language` using the `nonlocal` keyword.
"""def outerfunc():
    language='python'
    def innerfunc():
        nonlocal language # Change the value
        language='java'    
        print(language)    #prints the given updated language
    innerfunc()
outerfunc()"""

# 3 Write a function `outer()` that contains a variable `value = 10`. Inside it, define `inner1()` that changes `value` to `20` using `nonlocal`, and `inner2()` that just prints the value. Call them in sequence to check if changes persist.
"""
def outer():
    value=10
    def inner1():
        nonlocal value
        value=20
        print(value)
    def inner2():
        print(value)
    inner1()
    inner2()
outer()
"""
#Shadowing (both local and global)
# 1 Create a global variable `name = "Alice"`. Inside a function `print_name()`, define another variable `name = "Bob"` and print it. Then, print `name` outside the function and explain why they differ.
"""name='alice'
def names():
    name='bob'
    print(name)
names()
print(name)"""

# 2 Write a program where a local variable inside a function has the same name as a global variable, but the function still modifies the global variable by using the `global` keyword.
# ardam kale by chatgptttt.......
"""name='bob'
def local():
    global name
    name='bob'
    print(name)
local()
print(name) 
"""
#MIXED VARIABLE SCOPE
# 1 Write a function `bank_account()` that defines a variable `balance = 1000`. Inside it, define `deposit(amount)` and `withdraw(amount)` functions that modify `balance` using `nonlocal`. Add prints to see the updated balance after each operation.      
"""def bankaccc():
    balance=1000
    def deposit(amt):
        nonlocal balance 
        balance+=amt
        print(balance)
    deposit(300) #addinng 300 to balnce
    def withdraw(amt):
        nonlocal balance 
        balance-=amt
        print(balance)
    withdraw(900) #takig 200 from deposited amt =1300
bankaccc()"""

# 2 Create a program where: - You have a global variable `score`. - An outer function `game_round()` modifies `score` using `global`. - An inner function `bonus_points()` modifies a variable from the enclosing scope using `nonlocal`.
"""score=90
def game_round():
    global score 
    score=92
    bonus=10
    def bonus_points():
        nonlocal bonus
        bonus+=score
        print(bonus)
    bonus_points()
game_round()"""
#ardam ayinattu chesina but correct kadhu

val=20
def funcname():
    global val
    val=90
    print(val)
funcname()
print(val)

def outfunc():
    val=90
    def innerfunc():
        nonlocal val
        val=120
        print(val)
    innerfunc()
    print(val)
outfunc()
