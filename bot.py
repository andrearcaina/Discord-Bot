import os
import discord
from discord.ext import commands
from responses import respond
import asyncio

def run_bot(TOKEN,econ_bot):
    @econ_bot.event
    async def on_guild_join(guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send('Economy bot is here to steal your money! :dollar:')
            break

    @econ_bot.event
    async def on_ready():
        await econ_bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='the stock market | !help'))
        print(f'{econ_bot.user} running')

    @econ_bot.event
    async def on_message(message):
        print(f'{message.author} said: "{message.content}" ({message.channel})')
        try:
            if message.author == econ_bot.user:
                return
            
            user_message = str(message.content).lower()

            if '!' not in user_message: 
                for i in range(len(['map','where','idiot','bozo'])):
                    if ['map','where','idiot','bozo'][i] in user_message:
                        with open('map.png', 'rb') as f:
                            picture = discord.File(f)
                            await message.channel.send(file=picture)

                else:
                    rsp = respond(user_message,message.author)
                    await message.reply(rsp)
            else:
                await econ_bot.process_commands(message)
        except:
            print("not recognized bot response/command")

    @econ_bot.event
    async def on_command_error(ctx,error):
        if isinstance(error,commands.CommandOnCooldown):
            embed = discord.Embed(title=f":warning: Cooldown :warning:",description="**Still on cooldown**, please try again in {:.2f} seconds".format(error.retry_after),color=discord.Colour.yellow())
            await ctx.send(embed=embed)

    async def load():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await econ_bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"{filename[:-3]} is loaded")

    async def main():
        async with econ_bot:
            await load()
            await econ_bot.start(TOKEN)

    asyncio.run(main())