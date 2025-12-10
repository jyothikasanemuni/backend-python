import json
from addcards import addcards
from showcards import showcards
from spendcards import spendthecard
from paybill import paythebill

def main():
    print("click 1 for add the cards, click 2 for show the cards, click 3 for spend the cards, click 4 for pay the bill")
    choice=int(input("enter your choice: "))
    if choice==1:
        addcards()
    elif choice==2:
        showcards()
    elif choice==3:
        spendthecard()
    elif choice==4:
        paythebill()
    else:
        print("reenter the correct choice")
main()