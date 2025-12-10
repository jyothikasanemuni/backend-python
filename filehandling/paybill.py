import json
from load import load
def paythebill():
    card_number=int(input("enter credit card number: "))
    pay_amount=int(input("enter the amount you paid: "))
    data=load()
    found=False
    for i in data:
        if i['ccnum']==card_number:
            found=True
            if i['outstanding']<pay_amount:
                print("can't proess bcoz the outstanding is greater than the payable amount")
            else:
                i['cclimit']+=pay_amount
                i['outstanding']-=pay_amount
                print(f"hurray! the transaction is successfull,available limit is {i['cclimit']} and outstanding is {i['outstanding']}")
                break
    if not found:
        print("inavalid card number")
    with open("./creditcard.json","w") as f:
        json.dump(data,f,indent=4)
    print("pay the bills function is executing")