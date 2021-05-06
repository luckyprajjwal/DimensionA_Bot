import discord
import os
import datetime
from discord.ext import commands, tasks
from keepalive import keep_alive
import helper


client = discord.Client()
usual="Made by Dimensional Blade."


oday=2

@client.event
async def on_ready():
  # bg_task.start()
  print('A new dimension unfurled and the letter A emerges')

@client.event

async def on_message(message):
  if message.author==client.user:
    return

  await helper.parse_messages(message)




my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)



