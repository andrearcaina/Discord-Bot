import discord
from discord.ext import commands
from support import *

class Bunker(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('bunker commands are ready for use')

    @commands.command(aliases=["Bunker","bunk","Bunk","Stash","stash"])
    async def bunker(self,ctx):
        user_eco = open_account(ctx.author.id)

        shelter = user_eco[str(ctx.author.id)]['Shelter']

        if shelter:
            embed = discord.Embed(title=f"{ctx.author.name} Stash",color=discord.Colour.green())
            embed.add_field(name="Money:",value=f"${user_eco[str(ctx.author.id)]['Bunker']}",inline=True)
            embed.set_footer(text="shhh...",icon_url=None)
            await ctx.send(embed=embed)

    @commands.command(aliases=["create", "Build"])
    async def build(self,ctx):
        user_eco = open_account(ctx.author.id)

        vault = user_eco[str(ctx.author.id)]['Vault']
        shelter = user_eco[str(ctx.author.id)]['Shelter']

        if vault >= 5000000 and not shelter:
            user_eco[str(ctx.author.id)]['Shelter'] = True
            user_eco[str(ctx.author.id)]['Vault'] -= 5000000
            update_eco(user_eco)
            return await ctx.send("You have built a bunker. :bomb: :hut:\nYou can't get robbed now!")

        elif shelter:
            return await ctx.send("You already have a bunker!")

        else:
            return await ctx.send(":thinking:")
    
    @commands.command(aliases=["put", "Move","transfer","mo"])
    async def move(self,ctx,choice=None,amount=None):
        if choice == "in" or choice == "de" or choice == "deposit":
            user_eco = open_account(ctx.author.id)

            cur_vault = user_eco[str(ctx.author.id)]["Vault"]

            if amount == "all" and cur_vault > 0:
                user_eco[str(ctx.author.id)]["Vault"] -= cur_vault
                user_eco[str(ctx.author.id)]["Bunker"] += cur_vault

                update_eco(user_eco)

                await ctx.send(f"You have stashed {cur_vault} dollars to your bunker!")
                return
            
            if amount is None or amount == 0 or (amount == "all" and cur_vault == 0):
                await ctx.send("Please enter an amount to send.")
                return 

            amount = int(amount)

            if amount>cur_vault:
                await ctx.send("You don't have that much money in your vault!")
                return
            if amount<0:
                await ctx.send("Amount must be positive!")
                return
            
            user_eco[str(ctx.author.id)]["Vault"] -= amount
            user_eco[str(ctx.author.id)]["Bunker"] += amount

            update_eco(user_eco)

            await ctx.send(f"You have stashed {amount} dollars to your bunker!")
        elif choice == "out" or choice == "wi" or choice == "withdraw":
            user_eco = open_account(ctx.author.id)

            cur_bunk = user_eco[str(ctx.author.id)]["Bunker"] 

            if amount == "all" and cur_bunk > 0:
                user_eco[str(ctx.author.id)]["Vault"] += cur_bunk
                user_eco[str(ctx.author.id)]["Bunker"] -= cur_bunk

                update_eco(user_eco)

                await ctx.send(f"You have withdrawed {cur_bunk} dollars from your stash!")
                return

            if amount is None or amount == 0 or (amount == "all" and cur_bunk == 0):
                await ctx.send("Please enter an amount to send.")
                return 

            amount = int(amount)

            if amount>cur_bunk:
                await ctx.send("You don't have that much money in your stash!")
                return
            if amount<0:
                await ctx.send("Amount must be positive!")
                return
            
            user_eco[str(ctx.author.id)]["Vault"] += amount
            user_eco[str(ctx.author.id)]["Bunker"] -= amount

            update_eco(user_eco)

            await ctx.send(f"You have withdrawed {amount} dollars from your stash!")
        else:
            await ctx.send("Please choose 'in' or 'out' to move money\n in or out of your stash!")

async def setup(bot):
    await bot.add_cog(Bunker(bot))