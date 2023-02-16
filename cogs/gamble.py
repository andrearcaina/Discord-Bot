import discord
from discord.ext import commands
from support import *
from games import *
from random import randint
from blackjack import Blackjack

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('casino commands are ready for use')

    @commands.cooldown(1,2,commands.BucketType.user)
    @commands.command(aliases=["Roll", "rl"])
    async def roll(self,ctx,guess=None,amount=None):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]
        
        if guess is None:
            await ctx.send("Please send a guess. For additional help on this game, type !help roll")
            return

        guess = str(guess)

        if guess == "<7" or guess == "l" or guess == "=7" or guess == "e" or guess == ">7" or guess == "g":
            if amount == "all" and cur_bal > 0:
                user_eco[str(ctx.author.id)]["Balance"] -= cur_bal #pay first, then play
                write(user_eco)
                await play_roll(ctx,guess,cur_bal,user_eco)
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
            
            write(user_eco)
            await play_roll(ctx,guess,amount,user_eco)
        else:
            await ctx.send("That isn't an option! For help on this game, type !help roll.")

    @commands.cooldown(1,2,commands.BucketType.user)
    @commands.command(aliases=["cf","coinflip"])
    async def Coinflip(self,ctx,amount=None,choice="heads"):
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
    @commands.command(aliases=["slot","slots"])
    async def Slots(self,ctx,amount=None):
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

    @commands.command(aliases=["race","horserace","animalrace"])
    async def Race(self,ctx,choice=None,amount=None):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        if choice is None:
            embed = discord.Embed(title="Race :crown:",description="Please choose an animal (horse, dragon, trex, snail, tiger) to bet on.",color=discord.Colour.random())
            embed.set_footer(text=f"'!race [animal] [amount] to play. !help race for more info.",icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
            return

        choice = str(choice)

        if choice == "horse" or choice == "dragon" or choice == "trex" or choice == "snail" or choice == "tiger":
            if amount == "all" and cur_bal > 0:
                user_eco[str(ctx.author.id)]["Balance"] -= cur_bal #pay first, then play
                write(user_eco)
                await play_race(ctx,choice,cur_bal,user_eco)
                
            if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
                await ctx.send("Please enter an amount to send.")
                return 

            amount = int(amount)
            user_eco[str(ctx.author.id)]["Balance"] -= amount #pay first, then play

            if amount>cur_bal:
                await ctx.send("You don't have that much money!")
                return
            if amount<=0:
                await ctx.send("Amount must be positive and nonzero!")
                return

            write(user_eco)
            await play_race(ctx,choice,amount,user_eco)
        else:
            embed = discord.Embed(title="Race :crown:",description="Please choose an animal (horse, dragon, trex, snail, tiger) to bet on.",color=discord.Colour.random())
            embed.set_footer(text=f"!race [animal] [amount] to play. !help race for more info.",icon_url=ctx.author.avatar)
            await ctx.send(embed=embed)
            return

    @commands.cooldown(1,0,commands.BucketType.user)
    @commands.command(aliases=["blackjack","bj"])
    async def Blackjack(self,ctx,amount=None): 
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        if amount == "all" and cur_bal > 0:
            user_eco[str(ctx.author.id)]["Balance"] -= cur_bal #pay first, then play
            write(user_eco)
            await Blackjack().play_bj(ctx,cur_bal,user_eco)
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

        write(user_eco)
        await Blackjack().play_bj(ctx,amount,user_eco)
    
async def setup(bot):
    await bot.add_cog(Gamble(bot))