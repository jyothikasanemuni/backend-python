import json
from load import load
def spendthecard():
    card_number=int(input("enter credit card number: "))
    spend_amount=int(input("enter the amount you spend: "))
    data=load()
    found=False
    for i in data:
        if i['ccnum']==card_number:
            found=True
            if i['cclimit']<spend_amount:
                print("can't process bcoz the limit is less than the spend amt")
            else:
                i['cclimit']-=spend_amount
                i['outstanding']+=spend_amount
                print(f"hurray! the transaction is successfull,available limit is {i['cclimit']} and outstanding is {i['outstanding']}")
                break
    if not found:
        print("inavalid card number")
    with open("./creditcard.json","w") as f:
        json.dump(data,f,indent=4)
    print("spending the cards function is executing")