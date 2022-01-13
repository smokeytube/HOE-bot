import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
  @commands.command()
  async def hello(self, ctx):
    await ctx.send("Hello!")