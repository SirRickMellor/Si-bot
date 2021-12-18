import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from bs4 import BeautifulSoup
import requests
from replit import db

my_secret = os.environ['TOKEN']

bot = commands.Bot(command_prefix = "")

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.listen("on_message")
async def si(message): 
  if message.content.startswith("Sí"):
    await message.channel.send("xd Sí")


keep_alive()
bot.run(my_secret)
