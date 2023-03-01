import json
import discord

def update_eco(user_eco):
    with open("cogs/eco.json","w") as f:
        json.dump(user_eco,f,indent=4)

def update_bag(user_bag):
    with open("cogs/inventory.json","w") as f:
        json.dump(user_bag,f,indent=4)

def open_account(user):
    user_eco = json.load(open("cogs/eco.json","r"))

    if str(user) not in user_eco:
        user_eco[str(user)] = {}
        user_eco[str(user)]["Balance"] = 100
        user_eco[str(user)]["Vault"] = 0
        user_eco[str(user)]["In Game"] = False

        update_eco(user_eco)

    return user_eco

def open_bag(user):
    user_bag = json.load(open("cogs/inventory.json","r"))
    print("openingbag inventory.json")

    if str(user) not in user_bag:
        user_bag[str(user)] = {}
        user_bag[str(user)]["Fish"] = 0
        user_bag[str(user)]["Wolf"] = 0

        update_bag(user_bag)

    return user_bag

def multiHelp(pageNum=0,inline=False):
    helpGuide = json.load(open("help.json","r")) 
    pageNum = pageNum % len(list(helpGuide))
    pageTitle = list(helpGuide)[pageNum]
    
    embed = discord.Embed(title=pageTitle,color=discord.Colour.random())

    for key, val in helpGuide[pageTitle].items():
        embed.add_field(name=key,value=val,inline=inline)
        embed.set_footer(text=f"Page {pageNum+1} of {len(list(helpGuide))}")
    
    return embed