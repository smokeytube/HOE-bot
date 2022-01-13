import discord
from discord.ext import commands
from commands.admin import AdminCommands
from commands.general import GeneralCommands

bot = commands.Bot(command_prefix = '.')

bot.add_cog(AdminCommands())
bot.add_cog(GeneralCommands())




with open("TOKENDONOTCHECKIN.txt", 'r') as f:
    bot.run(f.read())