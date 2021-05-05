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


oday=2

def get_weekday(mode):
  day=datetime.date.today()
  d=day.weekday()
  if mode==1:
    d=d+1
  elif mode==-1:
    d=d-1
  elif mode==0:
    d=d
  if d<0:
    d=d+7
  elif d>6:
    d=d-7
  return d;
 

def get_message(d):
  global d0,d1,d2,d3,d4,d5
  if d>4:
    return d5;
  if d==0:
    return d0;
  if d==1:
    return d1;
  if d==2:
    return d2;
  if d==3:
    return d3;
  if d==4:
    return d4;
  
def get_dayname(d):
  x="UNKNOWN"
  if d==0:
    x="Monday"
  elif d==1:
    x="Tuesday"
  elif d==2:
    x="Wednesday"
  elif d==3:
    x="Thursday"
  elif d==4:
    x="Friday"
  elif d==5:
    x="Saturday"
  elif d==6:
    x="Sunday"
  return x

def get_colour(d):
  colour= discord.Color.from_rgb(255,255,255)
  if d==0:
    colour= discord.Color.from_rgb(238,130,238)
  elif d==1:
    colour= discord.Color.from_rgb(75,0,130)
  elif d==2:
    colour= discord.Color.from_rgb(0,0,205)
  elif d==3:
    colour= discord.Color.from_rgb(0,205,0)
  elif d==4:
    colour= discord.Color.from_rgb(205,205,0)
  elif d==5:
    colour= discord.Color.from_rgb(255,160,182)
  elif d==6:
    colour= discord.Color.from_rgb(205,0,0)
  return colour

@client.event
async def on_ready():
  bg_task.start()
  print('A new dimension unfurled and the letter A emerges')

@client.event

async def on_message(message):
  if message.author==client.user:
    return
  
  if message.content.startswith('$today'):
    d=get_weekday(0)
    await message.channel.send(embed=discord.Embed(title=get_dayname(d),description=get_message(d),color=get_colour(d)))
  if message.content.startswith('$monday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(0),description=get_message(0),color=get_colour(0)))
  if message.content.startswith('$tuesday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(1),description=get_message(1),color=get_colour(1)))
  if message.content.startswith('$wednesday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(2),description=get_message(2),color=get_colour(2)))
  if message.content.startswith('$thursday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(3),description=get_message(3),color=get_colour(3)))
  if message.content.startswith('$friday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(4),description=get_message(4),color=get_colour(4)))
  if message.content.startswith('$saturday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(5),description=get_message(5),color=get_colour(5)))
  if message.content.startswith('$sunday'):
    await message.channel.send(embed=discord.Embed(title=get_dayname(6),description=get_message(6),color=get_colour(6)))
  if message.content.startswith('$tomorrow'):
    d=get_weekday(1)
    await message.channel.send(embed=discord.Embed(title=get_dayname(d),description=get_message(d),color=get_colour(d)))
  if message.content.startswith('$yesterday'):
    d=get_weekday(-1)
    await message.channel.send(embed=discord.Embed(title=get_dayname(d),description=get_message(d),color=get_colour(d)))
  if message.content.startswith('$help'):
    await message.channel.send(embed=discord.Embed(title='Available commands',description=varhelp,color=discord.Color.from_rgb(100,100,100)))
  if message.content.startswith("$source"):
    await message.channel.send(src)
    await message.channel.send(usual)




@tasks.loop(seconds=14400)
async def bg_task():
  global oday

  channel=client.get_channel(839145616529424384)
  d=get_weekday(0)
  if d!=oday: 
    await channel.send(embed=discord.Embed(title=get_dayname(d),description=get_message(d),color=discord.Color.red()))
    oday=d
    
    print(oday)



my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)



