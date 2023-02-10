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

    @commands.command(aliases=["bal","b","Balance","Bal"])
    async def balance(self,ctx,member: discord.Member=None):
        # puts balance data into a json file for use (and automates it)
        user_eco = read()

        if member is None:
            member = ctx.author
        elif member is not None:
            member = member

        if str(member.id) not in user_eco:

            user_eco[str(member.id)] = {}
            user_eco[str(member.id)]["Balance"] = 100

            write(user_eco)

        embed = discord.Embed(title=f"{member.name}'s Current Balance",color=discord.Colour.green())
        embed.add_field(name="Balance:",value=f"${user_eco[str(member.id)]['Balance']}")
        embed.set_footer(text="Want to increase balance? go gamble or beg FOOL!",icon_url=None)
        await ctx.send(embed=embed)

    @commands.cooldown(1,3600,commands.BucketType.user)
    @commands.command(aliases=["Beg"])
    async def beg(self,ctx):
        user_eco = read()

        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100

            write(user_eco)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]
        amount = randint(-50,100)
        new_bal = cur_bal + amount
        print("current bal",cur_bal)
        print("amount given/taken",amount)
        print("new bal",new_bal)
        
        if new_bal < cur_bal:
            gang = ":ninja:"*3
            embed = discord.Embed(title="Oh no! you've been robbed!",description=f"A group of robbers saw an opportunity, and well, boom! {gang} UNLUCKY",color=discord.Colour.red())
            embed.add_field(name="Money lost:",value=f"${abs(amount)}",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="next time don't go to the yakuza for money",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] += amount

            write(user_eco)

        elif new_bal > cur_bal:
            money = ":money_with_wings:"*5
            embed = discord.Embed(title="Moneymonahmonaynonoymaoynoya!",description=money,color=discord.Colour.green())
            embed.add_field(name="Money gained:",value=f"${abs(amount)}",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="Want more? wait 1 hour to run this command again! (or try others)",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] += amount

            write(user_eco)

        elif new_bal == cur_bal+100:
            money = ":coin:"*5
            embed = discord.Embed(title="JACKPOTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT!",description=money,color=discord.Colour.gold())
            embed.add_field(name="Money gained:",value=f"${abs(amount)}",inline=False)
            embed.add_field(name="New Balance:",value=f"${new_bal}",inline=False)
            embed.set_footer(text="Want more? wait 1 hour to run this command again! (or try others)",icon_url=None)
            
            await ctx.send(embed=embed)

            user_eco[str(ctx.author.id)]["Balance"] += amount

            write(user_eco)

        elif new_bal == cur_bal:
            embed = discord.Embed(title="L bozo. get back to being homeless",description="begging ain't the best option. look at the map",color=discord.Colour.red())
            embed.set_footer(text="Want more? wait 1 hour to run this command again! (or try others)",icon_url=None)
            await ctx.send(embed=embed)

    @commands.cooldown(1,3600,commands.BucketType.user)       
    @commands.command(aliases=["w","Work"])
    async def work(self,ctx):
        user_eco = read()
        
        if str(ctx.author.id) not in user_eco:
            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100

            write(user_eco)
        
        amount = randint(100,200)
        user_eco[str(ctx.author.id)]["Balance"] += amount

        embed = discord.Embed(title=":briefcase::zzz:",description="After a long shift, here's what you earned!",color=discord.Colour.gold())
        embed.add_field(name="Earnings:",value=f"${amount}",inline=False)
        embed.add_field(name="New Balance:",value=f"${user_eco[str(ctx.author.id)]['Balance']}")
        embed.set_footer(text="Want more? wait 1 hour to run this command again! (or try others)",icon_url=None)

        write(user_eco)

        await ctx.send(embed=embed)

    @commands.cooldown(1,600,commands.BucketType.user)
    @commands.command(aliases=["r","Rob"])
    async def rob(self,ctx):
        user_eco = read()
        
        if str(ctx.author.id) not in user_eco:
            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100

            write(user_eco)

        cur_bal = user_eco[str(ctx.author.id)]["Balance"]
        amount = randint(200,3000)
        chance = randint(1,10)

        if chance <= 8:
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


async def setup(bot):
    await bot.add_cog(Economy(bot))