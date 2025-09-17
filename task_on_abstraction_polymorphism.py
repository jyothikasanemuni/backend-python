#  Polymorphism Tasks
#  1. Animals Speak Create a base class Animal with method sound(). Subclasses: - Dog → prints'Bark' - Cat → prints 'Meow' ,Create a list of animals and call sound() for each.
class animal:
    def sound(self):
        print("the animal sounds")
class dog(animal):
    def sound(self):
        print("the dog : barks")
class cat(animal):
    def sound(self):
        print("the cat : meows")
d=dog()
d.sound()
c=cat()
c.sound()

#  2. Calculator Operations Create a base class Calculator with method calculate(a, b). Subclasses: Add → adds two numbers - Subtract → subtracts two numbers  Call calculate() for both.
class calculator:
    def calculate(self,a,b):
        self.a=a
        self.b=b
class add(calculator):
    def calculate(self,a,b):
        print(f"the addition is {a+b}")
class subtract(calculator):
    def calculate(self,a,b):
        print(f"the subtraction : {a-b}")


A1=add()
A1.calculate(3,4)
A2=subtract()
A2.calculate(5,6)

#  3. Transport Ride Fare Class Transport with method fare(distance). Subclasses: - Bus → fare =distance * 10 - Train → fare = distance * 5 , Show polymorphism by calling fare() with same distance.
class transport:
    def fare(self,distance):
        self.distance=distance
class bus(transport):
    def fare(self,distance):
        print(f"the fare of bus is :{distance*10}")
class train(transport):
    def fare(self,distance):
        print(f"the fare of train is :{distance*5}")
b=bus()
b.fare(100)
t=train()
t.fare(100)

#  4. Shape Area Class Shape with method area(). Subclasses: - Square (side²) - Circle (π × r²) Loop through objects and print areas.
class shape:
    def area(self):
        pass
class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return f"the area of square is: {self.side*self.side}"
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self,radius):
        return f"the area of circle is: {3.14*self.radius*self.radius}"

shapes = [square(4), circle(7)]

for s in shapes:
    print(f"Area: {s.area()}")

#  5. Employee Work Class Employee with method work(). Subclasses: - Developer → prints 'Writing code' - Tester → prints 'Testing software'  Call work() on both employees.
class employee:
    def work(self):
        pass
class developer(employee):
    def work(self):
        print("writing code")
class tester(employee):
    def work(self):
        print("testing software")

d=developer()
d.work()
t=tester()
t.work()

# Abstraction Tasks
#  6. Vehicle Start Abstract class Vehicle with method start(). Subclasses: - Car → 'Car started' - Bike → 'Bike started'
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started")
class bike(vehicle):
    def start(self):
        print('bike started')
c=car()
c.start()
b=bike()
b.start()

#  7. Bank Account Abstract class BankAccount with method withdraw(amount). Subclasses: SavingsAccount → 'Withdrawn from savings' - CurrentAccount → 'Withdrawn from current'
from abc import ABC,abstractmethod
class bankacc(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
class savingsacc(bankacc):
    def withdraw(self,amount):
        print(f"withdraw from savings: {amount}")
class currentacc(bankacc):
    def withdraw(self,amount):
        print(f"withdraw from current: {amount}")   
s=savingsacc()
s.withdraw(200)
c=currentacc()
c.withdraw(1000)   

#  8. Device Power Abstract class Device with method power_on(). Subclasses: - TV → 'TV is ON' Laptop → 'Laptop is ON'
from abc import ABC,abstractmethod
class device(ABC):
    @abstractmethod
    def power_on(self):
        pass
class tv(device):
    def power_on(self):
        print("TV is on")
class laptop(device):
    def power_on(self):
       print("Laptop is on")
t=tv()
t.power_on()
l=laptop()
l.power_on()

#  9. Student Exam Abstract class Exam with method start_exam(). Subclasses: - MathExam → 'Math exam started' - EnglishExam → 'English exam started'
from abc import ABC,abstractmethod
class exam(ABC):
    @abstractmethod
    def start_exam(self):
        pass
class maths(exam):
    def start_exam(self):
        print("math exam is started")
class english(exam):
    def start_exam(self):
        print("english exam started")
m=maths()
m.start_exam()
e=english()
e.start_exam()
#  10. Report Generation Abstract class Report with method generate(). Subclasses: - PDFReport →'PDF Report generated' - ExcelReport → 'Excel Report generated'
from abc import ABC, abstractmethod
class report(ABC):
    @abstractmethod
    def generate(self):
        pass
class PDF(report):
    def generate(self):
        print("PDF Report generated")
class Excel(report):
    def generate(self):
        print("Excel Report generated")
p=PDF()
p.generate()
e=Excel()
e.generate()

