import discord
from discord.ext import commands
from support import *

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('regular commands are ready for use')

    @commands.command()
    async def blackjack(self,ctx,member:discord.Member = None):
        
        user_eco = read()

        if str(ctx.author.id) not in user_eco:

            user_eco[str(ctx.author.id)] = {}
            user_eco[str(ctx.author.id)]["Balance"] = 100

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