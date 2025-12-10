import json
def load():
    with open("./creditcard.json",'r') as f:
        data=json.load(f)
    return data