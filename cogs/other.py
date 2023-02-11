import discord
from support import *
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('misc commands are ready for use')

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Need Any Help?",description="All commands for the bot ↓↓↓",color=discord.Colour.random())

        embed.set_author(name="Economy Bot Commands!",icon_url=ctx.guild.icon.url)
        embed.add_field(name="Leaderboard :crown:",value="Check the top 5 richest people!",inline=True)
        embed.add_field(name="Ping :ping_pong:",value="Sends a pong message!",inline=True)
        embed.add_field(name="Casino Commands!",value="Gambling your money away!",inline=False)
        embed.add_field(name="Slots :t_rex:",value="Play slots for a chance to more money!",inline=True)
        embed.add_field(name="Blackjack :black_joker:",value="Play blackjack against the bot!",inline=True)
        embed.add_field(name="Economy Commands!",value="Get money!",inline=False)
        embed.add_field(name="Balance :dollar:",value="Check your wallet!",inline=True)
        embed.add_field(name="Deposit :dollar:",value="Deposit money to your vault!",inline=True)
        embed.add_field(name="Withdraw :dollar:",value="Withdraw money from your vault!",inline=True)
        embed.add_field(name="Send :moneybag:",value="Give money to other members!",inline=True)
        embed.add_field(name="Beg :coin:",value="Beg for money at Toronto!",inline=True)
        embed.add_field(name="Rob :ninja:",value="Rob for a chance of money!",inline=True)
        embed.add_field(name="Steal :atm:",value="Steal from other members!",inline=True)
        embed.add_field(name="Work :briefcase:",value="Work for 8 hours and get paid minimum wage!",inline=True)
        embed.set_footer(text=f'Requested by <@{ctx.author}>.',icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"Pong! :ping_pong: {round(self.bot.latency*1000)} ms.")

    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx, x=5):
        users = read()
        leaderboard = {}
        rank=[]
        
        for user in users:
            name = int(user)
            balance = users[str(user)]["Balance"] + users[str(user)]["Vault"]
            leaderboard[balance] = name
            rank.append(balance)
            
        rank = sorted(rank,reverse=True)

        embed = discord.Embed(title = f':money_mouth: Top {x} Richest People :money_mouth:',description = 'Decided by total cash of each person.',colour=discord.Colour.gold())
    
        i = 1
        for amount in rank:
            id_ = leaderboard[amount]
            member = self.bot.get_user(id_)
            embed.add_field(name = f'{i}: {member.name}', value = f'${amount}', inline=False)
            
            if i == x:
                break
            else:
                i += 1
            
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Help(bot))