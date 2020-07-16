import asyncio
import discord
import random
from discord.ext import commands

token = "        "

bot = commands.Bot(command_prefix=("!"), self_bot=True)

@bot.event
async def on_ready():
    print("Selfbot has been initiated")

@bot.command(pass_context=True)
async def e(ctx, message):
	content = ctx.message.content[3:]
	color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
	embedvar = discord.Embed(description=content, color=color)	
	await ctx.message.delete()
	await ctx.send(embed=embedvar)

bot.run(token, bot=False)

