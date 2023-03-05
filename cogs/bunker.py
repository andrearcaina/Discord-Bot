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

async def setup(bot):
    await bot.add_cog(Bunker(bot))