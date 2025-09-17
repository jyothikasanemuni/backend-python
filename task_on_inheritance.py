# #  Single Inheritance
# #  1. Bank Account System - Create a BankAccount class with attributes: account_number, balance.  Add methods: deposit(), withdraw(). - Create a child class SavingsAccount that adds an attribute.interest_rate and a method add_interest().
# class bankacc:
#     def __init__(self,acc_name,balance):
#         self.acc_name=acc_name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"the deposited amt is {self.balance}")
#     def withdraw(self,amount):
#         self.balance-=amount
#         print(f"the withdraw amt is {self.balance}")
# class savingsacc(bankacc):
#     def __init__(self,interest_rate,acc_name,balance):
#         self.interest_rate=interest_rate
#         self.acc_name=acc_name
#         self.balance=balance
#     def add_interest(self):
#         interest=self.balance*self.interest_rate/100
#         self.balance+=interest
#         print(f"interest added:{interest} ,new balance: {self.balance}")

# s1=savingsacc(34,"jyo",900)
# s1.deposit(500)
# s1.withdraw(100)
# s1.add_interest()
# # 2. Library Management - Parent class: Book with attributes title, author. - Child class: EBook with an extra attribute file_size and a method download().
# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def books(self):
#         print(f"the book tiltle is {self.title} and author is {self.author}")
# class ebook(book):
#     def __init__(self,title,author,file_size):
#         self.title=title
#         self.author=author
#         self.file_size=file_size
#     def download(self):
#         print(f"the title of the ebbok is {self.title},author is {self.author} and size is {self.file_size}")
# e1=ebook("To kill a mockingbird","Harper Lee","A4")
# e1.books()
# e1.download()
# #  3. Employee Management - Parent class: Employee with attributes name, salary. - Child class:Developer with an extra attribute programming_language.
# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class developer(employee):
#     def __init__(self,name,salary,programming_language):
#         self.name=name
#         self.salary=salary
#         self.programming_language=programming_language
#     def details(self):
#         print(f"Developer:{self.name}, salary:{self.salary}, good at:{self.programming_language}")
# d1=developer("jyothika","6LPA","python")
# d1.details()

# #  Multiple Inheritance
# #  4. Smartphone Features - Class Camera with method take_photo(). - Class MusicPlayer with method play_music(). - Class Smartphone (child) inherits from both Camera and MusicPlayer.
# class camera:
#     def take_photo(self):
#         print("the camera takes photos")
# class musicplayer:
#     def play_music(self):
#         print("The musicplayer plays music")
# class smartphone(camera,musicplayer):
#     pass
# s=smartphone()
# s.take_photo()
# s.play_music()

# #  5. Vehicle Features - Class Engine with method start_engine(). - Class Wheels with method ,rotate_wheels(). - Class Car inherits both and adds drive().
# class engine:
#     def start_engine(self):
#         print("engine started......")
# class wheels:
#     def rotate_wheels(self):
#         print("wheels rotate")
# class car(engine,wheels):
#     def drive(self):
#         print("we have to dive the car")
# c=car()
# c.drive()
# c.start_engine()
# c.rotate_wheels()     

# #  6. Hospital Management - Class Doctor with method treat_patient(). - Class Researcher with method conduct_research(). - Class DoctorResearcher inherits from both and can do both tasks.
# class doctor:
#     def treat_patient(self):
#         print("doctor treats patients")
# class researcher:
#     def conduct_research(self):
#         print("researchers do researchesss..")
# class doctorResearcher(doctor,researcher):
#     pass
# DR=doctorResearcher()
# DR.treat_patient()
# DR.conduct_research()

# Multi-level Inheritance
#  7. Educational Hierarchy - Class Person with attribute name. - Class Teacher inherits Person and adds subject. - Class HeadOfDepartment inherits Teacher and adds department_name.
class person:
    def __init__(self,name):
        self.name=name
class teacher(person):
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
class HOD(teacher):
    def __init__(self,name,subject,dept_name):
        self.name=name
        self.subject=subject
        self.dept_name=dept_name
    def details(self):
        print(f"Name: {self.name}, subject :{self.subject},department: {self.dept_name}")
h1=HOD("jyothika","COSM","CSE")
h1.details()
#  8. Online Shopping System - Product class with attributes name, price. - Electronics class inherits Product and adds brand. - Mobile class inherits Electronics and adds ram, storage.
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class elctronics(product):
    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand
class mobile(elctronics):
    def __init__(self, name, price, brand,ram,storage):
        self.name=name
        self.price=price
        self.brand=brand
        self.ram=ram
        self.storage=storage
    def details(self):
        print(f"NAME: {self.name},price :{self.price},brand:{self.brand},ram:{self.ram},storage:{self.storage}")
m=mobile("Samsung",20000,"F15","8GB",128)
m.details()
    
#  9. Transport System - Class Vehicle with attribute speed. - Class Car inherits Vehicle and adds fuel_type. - Class ElectricCar inherits Car and adds battery_capacity.
class vehicle:
    def __init__(self,speed):
        self.speed=speed
class car(vehicle):
    def __init__(self,speed,fuel_type):
        self.speed=speed
        self.fuel_type=fuel_type
class electriccar(car):
    def __init__(self,speed,fuel_type,battery_capacity):
        self.speed=speed
        self.fuel_type=fuel_type
        self.battery_capacity=battery_capacity
    def details(self):
        print(F"the speed: {self.speed}, fuel_type is :{self.fuel_type} and battery capacity is :{self.battery_capacity}")
e1=electriccar(120,"Diesel","250kmph")
e1.details()