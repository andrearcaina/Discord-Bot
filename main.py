import bot
import discord
from discord.ext import commands
from config import *
#from customhelp import CustomHelpCommand

if __name__ == "__main__":
    #initializing bot
    econ_bot = commands.Bot(command_prefix="!",help_command=None,intents=discord.Intents.all())
    #econ_bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())
    
    bot.run_bot(TOKEN,econ_bot)

    #this is just a useless file tbh
    #but it makes it 'clean'