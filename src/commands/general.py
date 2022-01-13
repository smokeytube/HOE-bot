import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
  @commands.command()
  async def hello(self, ctx):
    await ctx.send("Hello!")

  @commands.command()
  async def poll(self, ctx,*,message):
    emb=discord.Embed(title=message)
    ms = await ctx.channel.send(embed=emb)
    await ms.add_reaction('✅')
    await ms.add_reaction('❌')