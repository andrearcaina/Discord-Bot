import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('help commands are ready for use')

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Need Any Help?",description="All commands for the bot ↓↓↓",color=discord.Colour.random())

        embed.set_author(name="Economy Bot")
        embed.add_field(name="Ping :ping_pong:",value="Sends a pong message and the bot's ping.",inline=False)
        embed.add_field(name="Blackjack :black_joker:",value="Play blackjack against the bot!",inline=False)
        embed.add_field(name="Balance :dollar:",value="Check your wallet!",inline=False)
        embed.add_field(name="Beg :coin:",value="Beg for money at Toronto!",inline=False)
        embed.add_field(name="Rob :ninja:",value="Rob to get a chance of money!",inline=False)
        embed.add_field(name="Work :briefcase:",value="Work for 8 hours and get paid minimum wage!",inline=False)
        embed.set_footer(text=f'Requested by <@{ctx.author}>.',icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        ms = round(self.bot.latency*1000)
        await ctx.send(f"Pong! :ping_pong: {ms} ms.")

async def setup(bot):
    await bot.add_cog(Help(bot))