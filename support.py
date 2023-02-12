import json

def read():
    with open("cogs/eco.json","r") as f:
        user_eco = json.load(f)
    return user_eco    

def write(user_eco):
    with open("cogs/eco.json","w") as f:
        json.dump(user_eco,f,indent=4)

def open_account(user):
    user_eco = read()

    if str(user) not in user_eco:
        user_eco[str(user)] = {}
        user_eco[str(user)]["Balance"] = 100
        user_eco[str(user)]["Vault"] = 0

        write(user_eco)

    return user_eco