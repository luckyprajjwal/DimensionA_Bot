import discord
import os
import datetime
from discord.ext import commands, tasks
from keepalive import keep_alive


client = discord.Client()
#d=datetime.date.today()
usual="Made by Dimensional Blade."
#once="@everyone"
#print(d.weekday())
d0=os.environ['Monday']
d1=os.environ['Tuesday']
d2=os.environ['Wednesday']
d3=os.environ['Thursday']
d4=os.environ['Friday']
d5=os.environ['Nday']
varhelp=os.environ['help']
src=os.environ['src']


oday=1

def get_day():
  d=datetime.date.today()

  return (d)

def set_oday(dn):
 oday=dn

def get_oday():
  return oday



@client.event
async def on_ready():
  bg_task.start()
  print('A new dimension unfurled and the letter A emerges')

@client.event

async def on_message(message):
  d=get_day()
  if message.author==client.user:
    return
  
  if message.content.startswith('$today'):
    if d.weekday()>4:
      await message.channel.send(d5)
    elif d.weekday()==0:
      await message.channel.send(d0)
    elif d.weekday()==1:
      await message.channel.send(d1)
    elif d.weekday()==2:
      await message.channel.send(d2)
    elif d.weekday()==3:
      await message.channel.send(d3)
    elif d.weekday()==4:
      await message.channel.send(d4)    
    await message.channel.send(usual)
  if message.content.startswith('$monday'):
    await message.channel.send(d0)
    await message.channel.send(usual)
  if message.content.startswith('$tuesday'):
    await message.channel.send(d1)
    await message.channel.send(usual)
  if message.content.startswith('$wednesday'):
    await message.channel.send(d2)
    await message.channel.send(usual)
  if message.content.startswith('$thursday'):
    await message.channel.send(d3)
    await message.channel.send(usual)
  if message.content.startswith('$friday'):
    await message.channel.send(d4)
    await message.channel.send(usual)
  if message.content.startswith('$saturday'):
    await message.channel.send(d5)
    await message.channel.send(usual)
  if message.content.startswith('$sunday'):
    await message.channel.send(d6)
    await message.channel.send(usual)
  if message.content.startswith('$tomorrow'):
    if d.weekday()>3:
      await message.channel.send(d5)
    elif d.weekday()==6:
      await message.channel.send(d0)
    elif d.weekday()==0:
      await message.channel.send(d1)
    elif d.weekday()==1:
      await message.channel.send(d2)
    elif d.weekday()==2:
      await message.channel.send(d3)
    elif d.weekday()==3:
      await message.channel.send(d4)
  if message.content.startswith('$yesterday'):
    if d.weekday()==0:
      await message.channel.send(d5)
    elif d.weekday()==6:
      await message.channel.send(d5)
    elif d.weekday()==1:
      await message.channel.send(d0)
    elif d.weekday()==2:
      await message.channel.send(d1)
    elif d.weekday()==3:
      await message.channel.send(d2)
    elif d.weekday()==4:
      await message.channel.send(d3)
    elif d.weekday()==5:
      await message.channel.send(d4)
  if message.content.startswith('$help'):
    await message.channel.send(varhelp)
  if message.content.startswith("$source"):
    await message.channel.send(src)




@tasks.loop(seconds=14400)
async def bg_task():
  global oday

  channel=client.get_channel(839145616529424384)
  d=get_day()
  if d.weekday()!=oday:
    #await channel.send(once)
    if d.weekday()>4:
      await channel.send(d5)
    elif d.weekday()==0:
     await channel.send(d0)
    elif d.weekday()==1:
      await channel.send(d1)
    elif d.weekday()==2:
      await channel.send(d2)
    elif d.weekday()==3:
     await channel.send(d3)
    elif d.weekday()==4:
      await channel.send(d4)    
    
    await channel.send(embed=discord.Embed(title='title',description='desc',color=discord.Color.red()))
    oday=d.weekday()
    
    print(oday)



my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)



