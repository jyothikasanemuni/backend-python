import json
from load import load
def showcards():
    data=load()
    if data:
        print("Available credit cards are: ")
        for i in data:
            print(i)
    else:
        print("No cards are found")
    print("showcards function is executing")