import json
from load import load
def addcards():
    cards={"username":input("enter your username: "),"password":input("enter your password: "),"ccnum":int(input("enter Credit Card number: ")),"cclimit":int(input("enter Credit card Limit: ")),"outstanding":0
           }
    data=load()
    data.append(cards)
    with open("./creditcard.json","w") as f:
        json.dump(data,f,indent=4)
    print("Adding cards function is executing")