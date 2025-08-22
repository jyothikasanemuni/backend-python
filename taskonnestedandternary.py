#juice shop discount if a customer buys more than 2 bottles of juice if they are regular customer give fifteen percent discount if not give 5% discount
bottles=int(input("enter no.of bottles:"))
price_per_bottle=20
total=bottles*price_per_bottle
if bottles>2:
    discount=total*(15/100)
    print("you are a regular customer so 15% discount:",discount)
elif bottles<2:
    discount=(5/100)*total
    print("you got 5% discount ",discount)
else:
    print("no discount")
print("final amt:",total-discount)

#fuel check: if fuel=25% and if the vehicle is car print refuel soon at a petrol station if thevehicle is bike "refuel at nearest pump" print else print check vehicle type
fuel=input("enter fuel %: ")
vehicle=input("enter a vehicle type:")
if fuel==0.25:
    if vehicle=="car":
        print("refuel soon at a petrol station")
    elif vehicle=="bike":
        print("refuel at nearest pump")
    else:
        print("check vehicle type")
else:
    print("fuel is not 25%")

#scholarship eligibility : if student grade is above 85, if the income is below 3lakhs print eligible for scholarship if the income is b/w 3-6 lakhs print eligible for half scholarship else no scholarship
marks=int(input("enter your marks:"))
income=int(input("enter your income:"))
if marks>85:
    if income<300000:
        print("eligible for scholarship")
    elif 300000<=income<=600000:
        print("eligible for half scholarship")
    else:
        print("no scholarship")
else:
    print("marks are below 85 marks not eligible for scholarship")

#shopping cart :if cart value is over 1000, if the payment method is card 10% off,if the payment method is upi 15% off,else no discount.
cart=int(input("enter the cart value:"))
payment=input("enter the payment method:")
if cart>=1000:
    if payment=="card":
        discount=cart*(10/100)
        print("your paying by card so 10% off",discount)
    elif payment=="UPI":
        discount=cart*(15/100)
        print("your paying by upi so 15% off",discount)
    else:
        print("no discount")
else:
    print("your cart value is below 1000")
print("your total amt is:",cart-discount)

#restaurant entry check if age >=18: if vaccinated print"allowed to dine in" ,if not print"takeaway only" ,else you must be at leat 18 to dine here
age=int(input("enter your age:"))
vaccinated=input("enter yes or no:")
if age>=18:
    if vaccinated=="yes":
        print("you are allowed to dine in")
    else:
        print("takeaway only")
else:
    print("you must be at leat 18 to dine here ")

#sports tryouts: if the palyer age is b/w 14 to 18,if theheight is >160cm print "eligible",else "not eligible(too short) ,else: age is out of range..
age=int(input("enter your age:"))
height=int(input("enter your height:"))
if 14<=age<=18:
    if height>160:
        print("eligible")
    else:
        print("not eligible(too short)")
else:
    print("age is out of range....")

#PART B :TERNARY OPERATORS PROBLEMS
#TRAFFIC LIGHT : if light color is "green" print"go" ,else print"stop".
traffic_light_color=input("enter the light color:")
print("go" if traffic_light_color=="green" else "stop")

#MOVIE TICKET BASED ON AGE: if age >=18 "adult ticket",else "child ticket"
age=int(input("enter your age: "))
print("Adult ticket" if age>=18 else "child ticket")

#DISCOUNT OFFER: If amt spent is rs500 "you get a free gift" ,else "no gift".
amt=int(input("enter your spent amt: "))
print("gift" if amt>=500 else "no gift")

#DELIVERY FEE: if location is "local" -->rs20 delivery fee,else rs50 delivery fee
location=input("enter you location: ")
print("Delivery fee is RS:20" if location =="local" else "Delivery fee is RS:50")

#FEVER CHECK: if temperature>=100 "high fever" ,else "normal"
temp=int(input("enter your temperature: "))
print("High Fever" if temp>=100 else "Normal")

#(nested ternary)TIME-BASED GREETING: based on hour (24 hour format) <12 print "good mrng",<17 print "good afternoon",else "good evng"
time=int(input("enter the tym in 24-hour format: "))
print("good morning" if time<12 else "good afternoon" if time<17 else "good evening")

#BONUS CHALLENGE: ELECTRICITY BILL CALCULATOR : if units<100 print "free",if units b/w 100-300 : if usage is residential print "rs5 per unit" else(commercial) print "rs8 per unit" if units>300 : print("rs 10 per unit flat")
units=int(input("enter you units: "))
usage=input("enter if resdential(yes) or commercial(no): ")
if units<100:
    print("free")
elif 100<=units<=300:
    if usage=="yes":
        print("rs5 per unit")
    else:
        print("rs8 per unit")
elif units>300:
    print("rs10 per unit flat")