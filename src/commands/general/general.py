import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
  @commands.command()
  async def clear(self, ctx):
    await ctx.send("Hello!")