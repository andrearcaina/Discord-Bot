import discord
from discord.ext import commands
from support import *

class Inventory(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('inventory/fish/hunt/dig commands are ready for use')

    @commands.command(aliases=["Inventory","i","iven","iv","bag","Bag"])
    async def inventory(self,ctx,member: discord.Member=None):
        # puts balance data into a json file for use (and automates it)
        
        if member is None:
            member = ctx.author
        elif member is not None:
            member = member

        user_bag = open_bag(member.id)

        embed = discord.Embed(title=f"{member.name}'s Inventory",color=discord.Colour.green())
        embed.add_field(name="Fish:",value=f"{user_bag[str(member.id)]['Fish']}",inline=True)
        embed.add_field(name="Wolf:",value=f"{user_bag[str(member.id)]['Wolf']}",inline=True)
        embed.set_footer(text="Want to increase balance? go gamble or beg FOOL!",icon_url=None)
        await ctx.send(embed=embed)        

async def setup(bot):
    await bot.add_cog(Inventory(bot))