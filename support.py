import json
import discord

def read():
    return json.load(open("cogs/eco.json","r"))    

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

def multiHelp(pageNum=0,inline=False):
    helpGuide = json.load(open("help.json","r")) 
    pageNum = pageNum % len(list(helpGuide))
    pageTitle = list(helpGuide)[pageNum]
    
    embed = discord.Embed(title=pageTitle,color=discord.Colour.random())

    for key, val in helpGuide[pageTitle].items():
        embed.add_field(name=key,value=val,inline=inline)
        embed.set_footer(text=f"Page {pageNum+1} of {len(list(helpGuide))}")
    
    return embed