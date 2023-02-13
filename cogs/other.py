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
    async def help(self,ctx,choice=None):
        if choice is None:
            embed = discord.Embed(title="Need Any Help?",description="All commands for the bot ↓↓↓ !help [command_name] for more info!",color=discord.Colour.random())

            embed.set_author(name="Economy Bot Commands!",icon_url=ctx.guild.icon.url)

            #regular commands
            embed.add_field(name="Leaderboard :crown:",value="Check the top 5 richest people!",inline=True)
            embed.add_field(name="Ping :ping_pong:",value="Sends a pong message!",inline=True)
            
            #casino commands
            embed.add_field(name="Casino Commands!",value="Gamble money!",inline=False)
            embed.add_field(name="Slots :t_rex:",value="Play slots for a chance to more money!",inline=True)
            embed.add_field(name="Coinflip :dolphin:",value="Flip a coin for a chance to get double your bet!",inline=True)
            embed.add_field(name="Race :dragon:",value="Bet on an animal to get a chance of money!",inline=True)
            embed.add_field(name="Blackjack :black_joker:",value="Play blackjack against the bot! W.I.P",inline=True)
            
            #economy commands
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
        
        else: #if it is not None basically
            choice = str(choice)
            choice = choice.lower()

            if choice == "ping":
                embed = discord.Embed(title="Ping :ping_pong:",
                                    description="Type !ping to display pong message and bot ping.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'Have fun!",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "lb" or choice == "leaderboard":
                embed = discord.Embed(title="Leaderboard :crown:",
                                    description="Type !lb or !leaderboard to display the leaderboard.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'Ranked from most rich to most poor.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "slots" or choice == "slot":
                embed = discord.Embed(title="Slots :t_rex:",
                                    description="Type !slots [bet_amount] or !slot [bet_amount] for a chance to get nine times, triple or double your bet!",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!slots all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "coinflip" or choice == "cf":
                embed = discord.Embed(title="Coinflip :dolphin:",
                                    description="Type !cf [bet_amount] or !coinflip [bet_amount] for a chance to get double your bet!",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!cf all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "race":
                embed = discord.Embed(title="Race :dragon:",
                                    description="Type !race [animal] [amount] for a chance to get ten times your bet!\n\nAnimals: horse, dragon, trex, snail, tiger",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!race [animal] all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)
            
            elif choice == "send" or choice == "give":
                embed = discord.Embed(title="Send :moneybag:",
                                    description="Type !send @discordmember [amount] or !give @discordmember [amount] to send them money.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!send @discordmember all' will make you send your entire balance to the mentioned discord member.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "deposit" or choice == "dep":
                embed = discord.Embed(title="Deposit :dollar:",
                                    description="Type !deposit [amount] or !dep [amount] to deposit the amount into your vault.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!dep all' will make you deposit your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)
            
            elif choice == "withdraw" or choice == "wd" or choice == "with":
                embed = discord.Embed(title="Withdraw :dollar:",
                                    description="Type !withdraw [amount] or !with [amount] to withdraw that amount from your vault.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!with all' will make you withdraw your entire vault into your balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "rob":
                embed = discord.Embed(title="Rob :ninja:",
                                    description="Type !rob to rob money!",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"75% to 25% chance ... ",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "beg":
                embed = discord.Embed(title="Beg :coin:",
                                    description="Type !beg to beg for money!",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"you either lose money or gain money ...",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "work":
                embed = discord.Embed(title="Work :briefcase:",
                                    description="Type !work to work and gain a stable amount of money.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"not really ... ",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "steal":
                embed = discord.Embed(title="Steal :atm:",
                                    description="Type !steal @discordmember to steal their money!",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"Make sure you mention the user and replace 'discordmember' with their username.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            else:
                await ctx.send("That's not a command!")
                return

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