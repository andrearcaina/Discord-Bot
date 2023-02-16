import discord
from support import *
from discord.ext import commands
import asyncio

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.currentPage = 0

    @commands.Cog.listener()
    async def on_ready(self):
        print('misc commands are ready for use')

    @commands.command()
    async def help(self,ctx,choice=None):
        if choice is None:
            currentPage = 0
            buttons = ["⏮️","◀️","▶️","⏭"]

            msg = await ctx.send(embed=multiHelp(currentPage))
            
            for button in buttons:
                await msg.add_reaction(button)

            def check(reaction, user):    
                return str(reaction.emoji) in ["⏮️","◀️","▶️","⏭"] and user != self.bot.user

            while True:
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                    
                    if str(reaction.emoji) == buttons[3] and currentPage != 4:
                        currentPage = 4
                        await msg.edit(embed=multiHelp(currentPage))
                        await msg.remove_reaction(reaction, user)
                    
                    elif str(reaction.emoji) == buttons[2] and currentPage != 4:
                        currentPage += 1
                        await msg.edit(embed=multiHelp(currentPage))
                        await msg.remove_reaction(reaction, user)

                    elif str(reaction.emoji) == buttons[1] and currentPage > 0:
                        currentPage -= 1
                        await msg.edit(embed=multiHelp(currentPage))
                        await msg.remove_reaction(reaction, user)

                    elif str(reaction.emoji) == buttons[0] and currentPage != 0:
                        currentPage = 0
                        await msg.edit(embed=multiHelp(currentPage))
                        await msg.remove_reaction(reaction, user)

                    else:
                        await msg.remove_reaction(reaction, user)

                except asyncio.TimeoutError:
                    break

        else: #if it is not None basically
            choice = str(choice)
            choice = choice.lower()

            if choice == "ping":
                embed = discord.Embed(title="Ping :ping_pong:",
                                    description="Type !ping to display pong message and bot ping.",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"Have fun!",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "lb" or choice == "leaderboard":
                embed = discord.Embed(title="Leaderboard :crown:",
                                    description="Type !lb [choice] or !leaderboard [choice] to display \nthe leaderboard in the server or globally.\n\n For [choice], type either server or global.\nex: !lb server",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"Ranked from most rich to most poor.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "Roll" or choice == "roll" or choice == "rl":
                embed = discord.Embed(title="Roll <a:animated_dice:1075250955077038150>",
                                    description="Type !roll [guess] [bet_amount] or !rl [guess] [bet_amount]\nfor a chance to get five times or triple your bet!\nThis game is based off the dice game called Over Under 7.\n\nex: !rl <7 50\nex: !rl =7 50\nex: !rl >7 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"you can use 'l' instead of '<7' or \n'e' instead of '=7' or \n'g' instead of '>7' for your guess.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "slots" or choice == "slot":
                embed = discord.Embed(title="Slots :t_rex:",
                                    description="Type !slots [bet_amount] or !slot [bet_amount] for a chance\nto get nine times, triple or double your bet!\n\nex: !slots 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!slots all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "coinflip" or choice == "cf":
                embed = discord.Embed(title="Coinflip :dolphin:",
                                    description="Type !cf [bet_amount] or !coinflip [bet_amount] for a chance\nto get double your bet!\n\nex: !cf 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!cf all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "race":
                embed = discord.Embed(title="Race :snail:",
                                    description="Type !race [animal] [amount] for a chance to get ten times your bet!\n\nAnimals: horse, dragon, trex, snail, tiger\nex: !race snail 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!race [animal] all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)
            
            elif choice == "blackjack" or choice == "bj" or choice == "Blackjack":
                embed = discord.Embed(title="Blackjack :black_joker:",
                                    description="Type !blackjack [bet_amount] or !bj [bet_amount] for a chance to get triple or double times your bet!\n\nThis game is based off the traditional blackjack.\nYou can hit, double down, or stand.\nAnything above 21 is a bust!\n\nex: !bj 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!bj all' will make your bet_amount your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)
            
            elif choice == "send" or choice == "give":
                embed = discord.Embed(title="Send :moneybag:",
                                    description="Type !send @discordmember [amount] or\n!give @discordmember [amount] to send them money.\n\nex: !send @psykthe 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!send @discordmember all' will make you send\nyour entire balance to the mentioned discord member.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            elif choice == "deposit" or choice == "dep":
                embed = discord.Embed(title="Deposit :dollar:",
                                    description="Type !deposit [amount] or !dep [amount] to\ndeposit the amount into your vault.\n\nex: !dep 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!dep all' will make you deposit your current balance.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)
            
            elif choice == "withdraw" or choice == "wd" or choice == "with":
                embed = discord.Embed(title="Withdraw :dollar:",
                                    description="Type !withdraw [amount] or !with [amount] to\nwithdraw that amount from your vault.\n\nex: !with 50",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"'!with all' will make you withdraw your entire vault\ninto your balance.",icon_url=ctx.author.avatar)
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
                                    description="Type !steal @discordmember to steal their money!\n\nex: !steal @psykthe",
                                    color=discord.Colour.random())
                embed.set_footer(text=f"Make sure you mention the user and\nreplace 'discordmember' with their username.",icon_url=ctx.author.avatar)
                await ctx.send(embed=embed)

            else:
                await ctx.send("That's not a command!")
                return

    @commands.command(aliases=["Ping"])
    async def ping(self,ctx):
        await ctx.send(f"Pong! :ping_pong: {round(self.bot.latency*1000)} ms.")

    @commands.command(aliases=["Leaderboard","lb"])
    async def leaderboard(self, ctx, choice=None):
        if choice == "server":
            users = read()
            leaderboard = {}
            rank = []

            guild = self.bot.get_guild(ctx.message.guild.id)

            for user in users:
                name = int(user)
                balance = users[str(user)]["Balance"] + users[str(user)]["Vault"]
                if guild.get_member(name) is not None:
                    leaderboard[balance] = name
                    rank.append(balance)

            rank = sorted(rank,reverse=True)

            embed = discord.Embed(title = f':money_mouth: Top 3 Richest People :money_mouth:',description = 'Decided by total cash of each person.',colour=discord.Colour.gold())

            i = 1
            for amount in rank:
                id_ = leaderboard[amount]
                member = self.bot.get_user(id_)
                embed.add_field(name = f'{i}: {member.name}', value = f'${amount}', inline=False)
                
                if i == 3:
                    break
                else:
                    i += 1
                
            await ctx.send(embed = embed)
        
        elif choice == "global":
            users = read()
            leaderboard = {}
            rank = []

            for user in users:
                name = int(user)
                balance = users[str(user)]["Balance"] + users[str(user)]["Vault"]
                leaderboard[balance] = name
                rank.append(balance)

            rank = sorted(rank,reverse=True)

            embed = discord.Embed(title = f':money_mouth: Top 5 Richest People :money_mouth:',description = 'Decided by total cash of each person.',colour=discord.Colour.gold())
        
            i = 1
            for amount in rank:
                id_ = leaderboard[amount]
                member = self.bot.get_user(id_)
                embed.add_field(name = f'{i}: {member.name}', value = f'${amount}', inline=False)
                
                if i == 5:
                    break
                else:
                    i += 1
                
            await ctx.send(embed = embed)
        
        else:
            await ctx.send("Please specify between 'global' or 'server'.\nex: !lb server")

async def setup(bot):
    await bot.add_cog(Help(bot))