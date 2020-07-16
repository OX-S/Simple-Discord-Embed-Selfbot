#!/bin/bash
import asyncio
import discord
import random
from discord.ext import commands

token = "           "
whitelist = []

bot = discord.Client()

@bot.event
async def on_ready():
    print("Selfbot has been initiated")

@bot.event
async def on_message(message):
	if message.content.startswith("!e"):
		if message.author == bot.user:		
			content = message.content[3:]
			color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
			embedvar = discord.Embed(description=content, color=color)	
			await message.delete()
			await message.channel.send(embed=embedvar)
		elif str(message.author.id) in whitelist:
			content = message.content[3:]
			color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
			embedvar = discord.Embed(description=content, color=color)	
			await message.channel.send(embed=embedvar)
		else: 
			content = "You are not whitelisted on this selfbot."
			color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
			embedvar = discord.Embed(description=content, color=color)	
			await message.author.send(embed=embedvar)
	if message.content.startswith("!w"):
		if str(message.author) == str(bot.user):
			if "add" in message.content.lower():
				user = message.content[7:]
				if user in whitelist:
					content = "This user is already whitelisted!"
					color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
					embedvar = discord.Embed(description=content, color=color)	
					await message.channel.send(embed=embedvar)
				else:
					whitelist.append(user)
					content = "This user has been whitelisted."
					color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
					embedvar = discord.Embed(description=content, color=color)	
					await message.channel.send(embed=embedvar)
			elif "remove" in message.content.lower():
				user = message.content[10:]
				if user in whitelist:
					content = "This user has been removed from the whitelist."
					whitelist.remove(user)
					color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
					embedvar = discord.Embed(description=content, color=color)	
					await message.channel.send(embed=embedvar)
				else:
					content = "This user is not whitelisted."
					color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
					embedvar = discord.Embed(description=content, color=color)	
					await message.channel.send(embed=embedvar)
		else:
			content = "You do not have permission to do that command."
			color = discord.Color(value=int("%06x" % random.randint(0, 0xFFFFFF), 16))
			embedvar = discord.Embed(description=content, color=color)	
			await message.author.send(embed=embedvar)

		
bot.run(token, bot=False)
