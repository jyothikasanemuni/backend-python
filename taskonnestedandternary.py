#juice shop discount if a customer buys more than 2 bottles of juice if they are regular customer give fifteen percent discount if not give 5% discount
"""bottles=int(input("enter no.of bottles:"))
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
print("final amt:",total-discount)"""

#fuel check: if fuel=25% and if the vehicle is car print refuel soon at a petrol station if thevehicle is bike "refuel at nearest pump" print else print check vehicle type
"""fuel=input("enter fuel %: ")
vehicle=input("enter a vehicle type:")
if fuel==0.25:
    if vehicle=="car":
        print("refuel soon at a petrol station")
    elif vehicle=="bike":
        print("refuel at nearest pump")
    else:
        print("check vehicle type")
else:
    print("fuel is not 25%")"""

#scholarship eligibility : if student grade is above 85, if the income is below 3lakhs print eligible for scholarship if the income is b/w 3-6 lakhs print eligible for half scholarship else no scholarship
"""marks=int(input("enter your marks:"))
income=int(input("enter your income:"))
if marks>85:
    if income<300000:
        print("eligible for scholarship")
    elif 300000<=income<=600000:
        print("eligible for half scholarship")
    else:
        print("no scholarship")
else:
    print("marks are below 85 marks not eligible for scholarship")"""

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