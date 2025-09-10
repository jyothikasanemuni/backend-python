class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def enginestart(self):
        print(F"the {self.brand},{self.model} car has started")
        # print(f"the {self.brand} car has started")
    def enginestop(self):
        print(f"the {self.brand},{self.model} has stopped")

car1=Car("audi","A6")
# print(f"The brand of car is :{car1.model}")
car1.enginestart()
car1.enginestop()
car2=Car("lamborghini","avendator")
# print(f"the brand and model of the car2 is:{car2.brand},{car2.model}")
car2.enginestart()
car2.enginestop()

class food:
    def __init__(self,season,item):
        self.season=season
        self.item=item
    def seasonstart(self):
        print(f"The season {self.season} has started so the most purchased are {self.item}")
    def seasonend(self):
        print(f"The season {self.season} has ended")

Food1=food("summer","mango")
# print(f"The {Food1.season} is famous for {Food1.food}")
Food1.seasonstart()
Food1.seasonend()
Food2=food("rainy","raincoats & umbrellas")
# print(f"The {Food2.season} famous for: {Food2.food} ")
Food2.seasonstart()
Food2.seasonend()
Food3=food("winter","custard apples")
# print(f"The {Food3.season} famous for: {Food3.food} ")
Food3.seasonstart()
Food3.seasonend()

class clothings:
    def __init__(self,type,price):
        self.type=type
        self.price=price
    def startrange(self):
        print(f"the range of {self.type} is {self.price}")
    def discount(self):
         print(f"the discount for {self.type} is 50%")
    def discount1(self):
         print(f"the discount for {self.type} is 25%")
    def discount2(self):
         print(f"the discount for {self.type} is 75%")
clothing1=clothings("kurthis","400")
# print(f"the clothing is of type {clothing1.type} and price is {clothing1.price}")
clothing1.startrange()
clothing1.discount()
clothing2=clothings("sareees","2000")
clothing2.startrange()
clothing2.discount1()
# print(f"the clothing is of type {clothing2.type} and price is {clothing2.price}")
clothing3=clothings("coords","500")
# print(f"the clothing is of type {clothing3.type} and price is {clothing3.price}")
clothing3.startrange()
clothing3.discount2()

class homeappliances:
    def __init__(self,type,used):
        self.type=type
        self.used=used
    def use(self):
            print(f"the appliance {self.type} and it is used for {self.used}")
    def time(self):
         print(f"this appliance {self.type} is used daily")
home1=homeappliances("TV","Tvshows,serials,cinemas")
home1.use()
home1.time()
home2=homeappliances("kettle","waterheating")
home2.use()
home3=homeappliances("fridge","cooling")
home3.use()
home3.time()