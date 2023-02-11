import discord
from discord.ext import commands
from support import *
from random import randint

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('casino commands are ready for use')

    @commands.command(aliases=["slot"])
    async def slots(self,ctx,amount=None):
        user_eco = read()
        
        if str(ctx.author.id) not in user_eco:
            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100
            user_eco[str(ctx.author.id)]["Vault"] = 0

            write(user_eco)

        if amount is None:
            await ctx.send("Please enter an amount to send.")
            return 

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]
        amount = int(amount)

        if amount>cur_bal:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return
        
        # actual game
        slots = ["banana",
                 "apple",
                 "moneybag",
                 "dollar",
                 "ping_pong",
                 "crown",
                 "spy",
                ]

        slot1 = slots[randint(0,6)]
        slot2 = slots[randint(0,6)]
        slot3 = slots[randint(0,6)]
        slot4 = slots[randint(0,6)]
        slot5 = slots[randint(0,6)]
        slot6 = slots[randint(0,6)]
        slot7 = slots[randint(0,6)]
        slot8 = slots[randint(0,6)]
        slot9 = slots[randint(0,6)]

        print(slot1,slot2,slot3,slot4,slot5,slot6,slot7,slot8,slot9)

        slotOutput1 = '| :{}: | :{}: | :{}: |\n'.format(slot1,slot2,slot3)
        slotOutput2 = '| :{}: | :{}: | :{}: |\n'.format(slot4,slot5,slot6)
        slotOutput3 = '| :{}: | :{}: | :{}: |\n'.format(slot7,slot8,slot9)

        slot = ''.join([slotOutput1,slotOutput2,slotOutput3])

        pot = discord.Embed(title = "Slots Machine", color = discord.Colour.gold())
        pot.add_field(name = "{}\nJACKPOT".format(slot), value = f'You won {9*amount} dollars! :moneybag:',inline=False)

        won = discord.Embed(title = "Slots Machine", color = discord.Colour.green())
        won.add_field(name = "{}\nWon".format(slot), value = f'You won {3*amount} dollars! :dollar:',inline=False)
        
        mid = discord.Embed(title = "Slots Machine", color = discord.Colour.green())
        mid.add_field(name = "{}\nWon".format(slot), value = f'You won {2*amount} dollars! :coin:',inline=False)

        lost = discord.Embed(title = "Slots Machine", color = discord.Colour.red())
        lost.add_field(name = "{}\nLost".format(slot), value = f'You lost {1*amount} dollars. L bozo.',inline=False)

        if (slot1 == slot2 == slot3) and (slot4 == slot5 == slot6) and (slot7 == slot8 == slot9) or (slot1==slot2==slot3==slot4==slot5==slot6==slot7==slot8==slot9):
            user_eco[str(ctx.author.id)]["Balance"] += amount*9
            await ctx.send(embed = pot)
            return
        
        elif (slot1 == slot2 == slot3) or (slot4 == slot5 == slot6) or (slot7 == slot8 == slot9) or (slot1 == slot4 == slot7) or (slot2 == slot5 == slot8) or (slot3 == slot6 == slot9) or (slot1 == slot5 == slot9) or (slot3 == slot5 == slot7):
            user_eco[str(ctx.author.id)]["Balance"] += amount*3
            write(user_eco)
            await ctx.send(embed = won)
            return

        elif (slot1 == slot2) or (slot2 == slot3) or (slot4 == slot5) or (slot5 == slot6) or (slot7 == slot8) or (slot8 == slot9) or (slot1 == slot4) or (slot4 == slot7) or (slot2 == slot5) or (slot5 == slot8) or (slot3 == slot6) or (slot6 == slot9): 
            user_eco[str(ctx.author.id)]["Balance"] += amount*2
            write(user_eco)
            await ctx.send(embed = mid)
            return

        else:
            user_eco[str(ctx.author.id)]["Balance"] -= amount
            write(user_eco)
            await ctx.send(embed = lost)
            return

    @commands.command()
    async def blackjack(self,ctx,member:discord.Member = None):
        
        user_eco = read()

        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100
            user_eco[str(ctx.author.id)]["Vault"] = 0

            write(user_eco)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        

        if member == None:
            member = ctx.author
        
        name = member.display_name
        pfp = member.display_avatar

        embed = discord.Embed(title="Blackjack", description="W.I.P Blackjack", colour=discord.Colour.random())
        embed.set_author(name=f"{name}")
        embed.set_thumbnail(url=f"{pfp}")
        embed.add_field(name="Field 1", value="field value test")
        embed.add_field(name="2nd field", value="inline True", inline=True)
        embed.add_field(name="rdd3 feild", value="false inline", inline=False)
        embed.set_footer(text=f"{name} wwaassz")
        
        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(Gamble(bot))