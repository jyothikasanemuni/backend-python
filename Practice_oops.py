# ✅ Task 1: Student Information System
# Concepts Covered: class, object, __init__, instance method
# Problem Statement:
# Create a class Student with: - __init__(self, name, roll, marks) - A method display() that prints student details
# Expected Output:
# Name: Manoj
# Roll: 101
# Marks: 85
# Hint:
class Student:
    def __init__(self, name, roll, marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print(f"{self.name} roll number is {self.roll} got {self.marks} marks")
s1=Student("Manoj",101,85)
s1.display()

# ✅ Task 2: Bank Account Management
# Problem Statement:Create a class BankAccount with: - __init__(self, name, balance) - deposit(amount) - withdraw(amount) - show_balance()
# Rules:
# Withdrawal amount should not exceed balance
# Display appropriate messages
# Sample Output:
# Deposited: 1000
# Current Balance: 5000
class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"The deposited amt is {amount} and the total is {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"The withdraw amt is {amount}")
        else:
            print("insufficient balance")
    def remaining(self):
        print(f"the ramaining balance is {self.balance}")

b1=bank("jyothika",2000)
b1.deposit(2000)
b1.withdraw(500)
b1.remaining()


# ✅ Task 3: Rectangle Calculator
# Create a class Rectangle with: - __init__(self, length, width) - area() → returns area - perimeter() → returns perimeter
# Sample Output:
# Area: 50
# Perimeter: 30
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        print(F"the area of rectangel is {area}")
    def perimeter(self):
        perimeter=((2*self.length)+(2*self.breadth))
        print(F"The perimeter of rectangle is {perimeter}")
r1=rectangle(50,30)
r1.area()
r1.perimeter()

# ✅ Task 4: Employee Salary System
# Create a class Employee with: - __init__(self, name, salary) - increase_salary(percent) - display()
# Sample Output:
# Name: Ravi
# Updated Salary: 55000
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increase_salary(self,percent):
        updated_salary=self.salary+(self.salary*percent/100)
        print(f"the updated salary is: {updated_salary}")
    def display(self):
        print(F"Name: {self.name}, old salary: {self.salary}")
e1=employee("ravi",30000)
e1.display()
e1.increase_salary(30)

# ✅ Task 5: User Login System
# Create a class User with: - __init__(self, username, password) - login(input_username, input_password)
# Conditions:
# Print "Login Successful" if credentials match
# Else print "Invalid Credentials"
class userlogin:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self):
        if self.username=="admin12" and self.password=="admin@123":
            print("login successfull")
        else:
            print("worng credentials")
u1=userlogin("admin12","admin@123")
u1.login()
