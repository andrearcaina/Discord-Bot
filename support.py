import json

def read():
    with open("cogs/eco.json","r") as f:
        user_eco = json.load(f)
    return user_eco    

def write(user_eco):
    with open("cogs/eco.json","w") as f:
        json.dump(user_eco,f,indent=4)
