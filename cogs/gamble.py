import discord
from discord.ext import commands
from support import *
from games import *
from random import randint

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('casino commands are ready for use')

    @commands.cooldown(1,2,commands.BucketType.user)
    @commands.command(aliases=["cf"])
    async def coinflip(self,ctx,amount=None,choice="heads"):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        choice = choice.lower()
        
        numb = randint(1,2)

        if amount == "all" and cur_bal > 0:
            user_eco[str(ctx.author.id)]["Balance"] -= cur_bal #pay first, then play
            await play_cf(ctx,choice,numb,cur_bal,user_eco)
            return
            
        if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
            await ctx.send("Please enter an amount to send.")
            return 

        amount = int(amount)
        user_eco[str(ctx.author.id)]["Balance"] -= amount #pay first, then play

        if amount>cur_bal:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return
        
        await play_cf(ctx,choice,numb,amount,user_eco)

    @commands.cooldown(1,2,commands.BucketType.user)
    @commands.command(aliases=["slot"])
    async def slots(self,ctx,amount=None):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        if amount == "all" and cur_bal > 0:
            user_eco[str(ctx.author.id)]["Balance"] -= cur_bal #pay first, then play
            await play_slots(ctx,cur_bal,user_eco)
            return
            
        if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
            await ctx.send("Please enter an amount to send.")
            return 

        amount = int(amount)
        user_eco[str(ctx.author.id)]["Balance"] -= amount #pay first, then play

        if amount>cur_bal:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return

        await play_slots(ctx,amount,user_eco)

    @commands.command(aliases=["horserace","animalrace"])
    async def race(self,ctx,choice=None,amount=None):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        if choice is None:
            embed = discord.Embed(title="Race :crown:",description="Please choose an animal (horse, dragon, dino, snail, tiger) to bet on.",color=discord.Colour.random())
            embed.set_footer(text=f"'!race [animal] [amount] to play.",icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
            return

        else:
            if amount == "all" and cur_bal > 0:
                user_eco[str(ctx.author.id)]["Balance"] -= cur_bal #pay first, then play
                write(user_eco)
                await play_race(ctx,choice,cur_bal,user_eco)
                
            if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
                await ctx.send("Please enter an amount to send.")
                return 

            amount = int(amount)
            user_eco[str(ctx.author.id)]["Balance"] -= amount #pay first, then play
            write(user_eco)

            if amount>cur_bal:
                await ctx.send("You don't have that much money!")
                return
            if amount<0:
                await ctx.send("Amount must be positive!")
                return

            await play_race(ctx,choice,amount,user_eco)

    @commands.command()
    async def blackjack(self,ctx,member:discord.Member = None):
        user_eco = open_account(ctx.author.id)

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