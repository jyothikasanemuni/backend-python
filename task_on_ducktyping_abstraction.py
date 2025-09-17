# Task:
# Duck Typing Tasks
# 1. Walk Like a Duck :Create two classes Duck and Person, Both should have a method walk().Write a function make_it_walk(obj) that accepts any object and calls walk(). Pass objects of both classes and observe.
class duck:
    def walk(self):
        print("duck walks")
duck1=duck()
class person:
    def walk(self):
        print("person walks")
p1=person()
def make_it_walk(obj):
    obj.walk()
make_it_walk(duck1)
make_it_walk(p1)

# 2. Media Player Example
# Create two classes:MP3 → with method play() ,Video → with method play(). Write a function start_media(obj) to call play() no matter the type.
class MP3:
    def play(self):
        print("MP3 plays audio like music")
mp3=MP3()
class video:
    def play(self):
        print("video plays")
v1=video()
def start_media(obj):
    obj.play()
start_media(mp3)
start_media(v1)

# 3. Payment System Create two classes:CreditCard → with method pay(amount) ,UPI → with method pay(amount). Write a function process_payment(obj, amount) to call pay().
class creditcard:
    def pay(self,amount):
        print(f"the creditcard has amt: {amount}")
cc=creditcard()
class UPI:
    def pay(self,amount):
        print(f"By UPI, the limit of amt is {amount}")
upi=UPI()
def process_payment(obj,amount):
    obj.pay(amount)
process_payment(cc,500)
process_payment(upi,1000)

# Abstraction Tasks
# 4. Shape Area (Abstract): Create an abstract class Shape with an abstract method area(). Subclasses:Square → calculates side², Circle → calculates π × r²
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"the area of square : {self.side*self.side}")
sq=square(5)
sq.area()
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"the area of circle is :{3.14*self.radius*self.radius}")
c=circle(4)
c.area()
# 5. Vehicle Start (Abstract): Create an abstract class Vehicle with an abstract method start(). Subclasses:Car → prints "Car started" Bike → prints "Bike started"
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started")
c=car()
c.start()
class bike(vehicle):
    def start(self):
        print("bike started")
b=bike()
b.start()

# # 6. Bank Account (Abstract): Create an abstract class BankAccount with abstract method withdraw(amount). Subclasses: SavingsAccount → withdraw allowed if balance > 500, CurrentAccount → no minimum balance check
# from abc import ABC,abstractmethod
# class bankacc(ABC):
#     @abstractmethod
#     def withdraw(self,amount):
#         pass
# class savingsacc(bankacc):
#     def withdraw(self,amount):
#         if 
# 7. Report Generation (Abstract): Create an abstract class Report with abstract method generate(). Subclasses: PDFReport → prints "PDF Report generated", ExcelReport → prints "Excel Report generated"
from abc import ABC,abstractmethod
class report(ABC):
    @abstractmethod
    def generate(self):
        pass
class pdfreport(report):
    def generate(self):
        print("PDF report generated")
class excel(report):
    def generate(self):
        print("excel report generated")
pdf=pdfreport()
pdf.generate()
Excel=excel()
Excel.generate()
# 8. Employee Work (Abstract): Create an abstract class Employee with an abstract method work(). Subclasses: Developer → prints "Writing code", Tester → prints "Testing software"
from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def work(self):
        pass
class developer(employee):
    def work(self):
        print("writing code")
class tester(employee):
    def work(self):
        print("testing software")
d1=developer()
d1.work()
t1=tester()
t1.work()

# 9. Appliance Power (Abstract): Create an abstract class Appliance with abstract method turn_on(). Subclasses:Fan → prints "Fan is ON", Light → prints "Light is ON"
from abc import ABC,abstractmethod
class appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class fan(appliance):
    def turn_on(self):
        print("Fan is ON")
class light(appliance):
    def turn_on(self):
        print("Light is ON")
f1=fan()
f1.turn_on()
l1=light()
l1.turn_on()


