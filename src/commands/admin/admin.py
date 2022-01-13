import discord
from discord.ext import commands

class AdminCommands(commands.Cog):
  @commands.command()
  @commands.has_permissions(administrator = True)
  async def clear(self, ctx, amount=2):
    await ctx.channel.purge(limit=amount)

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"User {member} **has been kicked now he will be homeless, boss**")

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason) 
    await ctx.send(f"User {member} **has been banned, we destroyed his life, boss**")