import discord
from discord.ext import commands
from support import *
from random import randint

class Economy(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('economy commands are ready for use')

    @commands.command(aliases=["bal","b","Balance","Bal","Vault","vault"])
    async def balance(self,ctx,member: discord.Member=None):
        # puts balance data into a json file for use (and automates it)
        
        if member is None:
            member = ctx.author
        elif member is not None:
            member = member

        user_eco = open_account(member.id)

        embed = discord.Embed(title=f"{member.name}'s Current Balance",color=discord.Colour.green())
        embed.add_field(name="Balance:",value=f"${user_eco[str(member.id)]['Balance']}",inline=True)
        embed.add_field(name="Vault:",value=f"${user_eco[str(member.id)]['Vault']}",inline=True)
        embed.set_footer(text="Want to increase balance? go gamble or beg FOOL!",icon_url=None)
        await ctx.send(embed=embed)

    @commands.command(aliases=["Send","give","grant"])
    async def send(self,ctx,member:discord.Member,amount = None):
        user_eco = open_account(ctx.author.id)
        user_eco = open_account(member.id)

        if ctx.author.id == member.id:
            await ctx.send("You can't send yourself money!")
            return 

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        if amount == "all" and cur_bal > 0:
            user_eco[str(ctx.author.id)]["Balance"] -= cur_bal
            user_eco[str(member.id)]["Balance"] += cur_bal

            write(user_eco)

            member = str(member)[:-5]
            await ctx.send(f"You have given {cur_bal} dollars to {member}!")
            return
            
        if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
            await ctx.send("Please enter an amount to send.")
            return 

        if amount is None:
            await ctx.send("Please enter an amount to send.")
            return 

        amount = int(amount)

        if amount>cur_bal:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return
        
        user_eco[str(ctx.author.id)]["Balance"] -= amount
        user_eco[str(member.id)]["Balance"] += amount

        write(user_eco)

        member = str(member)[:-5]
        await ctx.send(f"You have given {amount} dollars to {member}!")

    @commands.cooldown(1,60,commands.BucketType.user)
    @commands.command(aliases=["Beg"])
    async def beg(self,ctx):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]
        amount = randint(-50,100)
        new_bal = cur_bal + amount
        
        if cur_bal == 0:
            gang = ":ninja:"*3
            embed = discord.Embed(title="Oh no! you've been robbed!",description=f"A group of robbers saw an opportunity, and well, boom! {gang} UNLUCKY",color=discord.Colour.red())
            embed.add_field(name="Money lost:",value=f"none. You had no money on you.",inline=False)
            embed.set_footer(text="next time don't go to the yakuza for money",icon_url=None)
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] = 0

        if 20 <= cur_bal <= 50:
            gang = ":ninja:"*3
            embed = discord.Embed(title="Oh no! you've been robbed!",description=f"A group of robbers saw an opportunity, and well, boom! {gang} UNLUCKY",color=discord.Colour.red())
            embed.add_field(name="Money lost:",value=f"${abs(cur_bal)}",inline=False)
            embed.add_field(name="New Balance:",value="$0",inline=False)
            embed.set_footer(text="next time don't go to the yakuza for money",icon_url=None)
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] = 0

            write(user_eco)

        if cur_bal > 50 and new_bal < cur_bal:
            gang = ":ninja:"*3
            embed = discord.Embed(title="Oh no! you've been robbed!",description=f"A group of robbers saw an opportunity, and well, boom! {gang} UNLUCKY",color=discord.Colour.red())
            embed.add_field(name="Money lost:",value=f"${abs(amount)}",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="next time don't go to the yakuza for money",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] += amount

            write(user_eco)

        elif cur_bal > 50 and new_bal > cur_bal:
            money = ":money_with_wings:"*5
            embed = discord.Embed(title="Some kind souls are kind to a nobody like you!",description=money,color=discord.Colour.green())
            embed.add_field(name="Money gained:",value=f"${abs(amount)}",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="Want more? wait 1 minute to run this command again! (or try others)",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] += amount

            write(user_eco)

        elif new_bal == cur_bal:
            embed = discord.Embed(title="L bozo. get back to being homeless",description="begging ain't the best option. look at the map",color=discord.Colour.red())
            embed.set_footer(text="Want more? wait 1 minute to run this command again! (or try others)",icon_url=None)
            await ctx.send(embed=embed)

    @commands.cooldown(1,3600,commands.BucketType.user)       
    @commands.command(aliases=["w","Work"])
    async def work(self,ctx):
        user_eco = open_account(ctx.author.id)
        
        amount = randint(100,200)
        user_eco[str(ctx.author.id)]["Balance"] += amount

        embed = discord.Embed(title=":briefcase::zzz:",description="After a long shift, here's what you earned!",color=discord.Colour.gold())
        embed.add_field(name="Earnings:",value=f"${amount}",inline=False)
        embed.add_field(name="New Balance:",value=f"${user_eco[str(ctx.author.id)]['Balance']}")
        embed.set_footer(text="Want more? wait 1 hour to run this command again! (or try others)",icon_url=None)

        write(user_eco)

        await ctx.send(embed=embed)

    @commands.cooldown(1,3600,commands.BucketType.user)
    @commands.command(aliases=["s","st"])
    async def steal(self,ctx,member:discord.Member):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(member.id)]["Balance"]
        if cur_bal<100:
            await ctx.send("It's not worth getting that!")
            return
        
        stolen = randint(0,cur_bal)
    
        user_eco[str(ctx.author.id)]["Balance"] += stolen
        user_eco[str(member.id)]["Balance"] -= stolen

        write(user_eco)

        member = str(member)[:-5]
        await ctx.send(f"You stole ${stolen} from {member}!")


    @commands.cooldown(1,600,commands.BucketType.user)
    @commands.command(aliases=["r","Rob"])
    async def rob(self,ctx):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]
        amount = randint(200,3000)
        chance = randint(1,20)

        if cur_bal<=100:
            await ctx.send("Not worth risking your money!")
            return

        if cur_bal > 100 and chance <= 15: #75% chance
            new_bal = cur_bal - 500
            embed = discord.Embed(title="YOU GOT CAUGHT!",description="Fortunately for you, they let you off with a small fine. :police_officer::oncoming_police_car:",color=discord.Colour.red())
            embed.add_field(name="Money lost:",value="$500",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="Want to commit more crime? wait 10 minutes to run this command again! (or try others)",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] -= 500

            write(user_eco)
        else:
            new_bal = cur_bal + amount
            embed = discord.Embed(title="YOU Sneaky bastard!",description="sheesh. bro got out :ninja::money_with_wings:",color=discord.Colour.green())
            embed.add_field(name="Money gained:",value=f"${amount}",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="Want to commit more crime? wait 10 minutes to run this command again! (or try others)",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] += amount

            write(user_eco)

    @commands.command(aliases=["withdraw","wi","with","wd"])
    async def Withdraw(self,ctx,amount=None):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Vault"] 

        if amount == "all" and cur_bal > 0:
            user_eco[str(ctx.author.id)]["Balance"] += cur_bal
            user_eco[str(ctx.author.id)]["Vault"] -= cur_bal

            write(user_eco)

            await ctx.send(f"You have withdrawed {cur_bal} dollars from your vault!")
            return

        if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
            await ctx.send("Please enter an amount to send.")
            return 

        amount = int(amount)

        if amount>cur_bal:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return
        
        user_eco[str(ctx.author.id)]["Balance"] += amount
        user_eco[str(ctx.author.id)]["Vault"] -= amount

        write(user_eco)

        await ctx.send(f"You have withdrawed {amount} dollars from your vault!")
    
    @commands.command(aliases=["deposit","d","de","dep"])
    async def Deposit(self,ctx,amount=None):
        user_eco = open_account(ctx.author.id)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]

        if amount == "all" and cur_bal > 0:
            user_eco[str(ctx.author.id)]["Balance"] -= cur_bal
            user_eco[str(ctx.author.id)]["Vault"] += cur_bal

            write(user_eco)

            await ctx.send(f"You have deposited {cur_bal} dollars to your vault!")
            return
        
        if amount is None or amount == 0 or (amount == "all" and cur_bal == 0):
            await ctx.send("Please enter an amount to send.")
            return 

        amount = int(amount)

        if amount>cur_bal:
            await ctx.send("You don't have that much money!")
            return
        if amount<0:
            await ctx.send("Amount must be positive!")
            return
        
        user_eco[str(ctx.author.id)]["Balance"] -= amount
        user_eco[str(ctx.author.id)]["Vault"] += amount

        write(user_eco)

        await ctx.send(f"You have deposited {amount} dollars to your vault!")

async def setup(bot):
    await bot.add_cog(Economy(bot))