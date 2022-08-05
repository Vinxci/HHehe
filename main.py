import os
import discord
from discord.ext import commands
from secret import TOKEN
bot = commands.Bot(command_prefix = ")")

@bot.event
async def on_ready():
  print("Bot ready")

@bot.command()
async def hello(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/689591708962652289/1002649255695097866/Ruptured_Rollercoaster.webm")

@bot.command()
async def kriss(ctx):
  await ctx.reply("https://tenor.com/bIjgC.gif")
    
@bot.command()
async def troll(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/1004055744389316620/1004085412203077642/rickroll.mp4")

@bot.command()
async def alive(ctx):
    await ctx.reply("@everyone")

@bot.command()
async def frog(ctx):
    await ctx.reply("https://cdn.discordapp.com/attachments/1004055744389316620/1004084267149701210/frog..mp4")

@bot.command()
async def purge(ctx):
    msg = ctx.content.split()
    count = msg[-1]
    try:
      count = int(count)
    except:
      await ctx.reply("How many messages?")
      return
    await ctx.channel.purge(limit = count) 
    await ctx.reply("Messages deleted")

@bot.command()
async def iam(ctx, *, role_name: str):
    
  for role in ctx.guild.roles:
      if role.name == role_name:
        await ctx.author.add_roles(role)
        await ctx.reply("Role added!")
        return
        
  await ctx.reply("Invalid role")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason"):
        await user.ban(reason=reason)
        embed = discord.Embed(color=discord.Colour.red(),title="", description="")
        embed.add_field(name="Banned:", value=f"""
The user **{user}** has been banned.
Reason = **{reason}**
""", inline=True)
        await ctx.reply(embed=embed)

bot.run(TOKEN)