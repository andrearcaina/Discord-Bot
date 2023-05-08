import os
import discord
from discord.ext import commands
import asyncio

def run_bot(TOKEN,econ_bot):
    @econ_bot.event
    async def on_guild_join(guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send('Economy bot is here to steal your money! type !help :dollar:')
            break

    @econ_bot.event
    async def on_ready():
        await econ_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='the stock market | !help'))
        print(f'{econ_bot.user} is now running')

    @econ_bot.event
    async def on_message(message):
        print(f'{message.author} said: "{message.content}" ({message.channel})')
        user_message = str(message.content).lower()

        if '!' not in user_message: 
            for i in range(13):
                if ['map','where','idiot','bozo','broke'][i] in user_message:
                    with open('map.png', 'rb') as f:
                        picture = discord.File(f)
                        await message.channel.send(file=picture)
                        return
                elif ['cgpa', 'gpa', 'cum', 'cumulative', 'grade', 'point', 'average'][i] in user_message:
                    with open('cgpa.png', 'rb') as f:
                        picture = discord.File(f)
                        await message.channel.send(file=picture)
                        return
        else:
            await econ_bot.process_commands(message)

    @econ_bot.event
    async def on_command_error(ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            embed = discord.Embed(title=f":warning: Cooldown :warning:",description="**Still on cooldown**, please try again in {:.2f} seconds <@{}>!".format(error.retry_after,ctx.author),color=discord.Colour.yellow())
            await ctx.send(embed=embed)

    async def load():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await econ_bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"{filename[:-3]} is loading...")

    async def main():
        async with econ_bot:
            await load()
            await econ_bot.start(TOKEN)

    asyncio.run(main())