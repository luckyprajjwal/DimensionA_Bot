import discord
import os
import datetime
from discord.ext import commands, tasks
from keepalive import keep_alive
import helper
import data


client = discord.Client()
#d=datetime.date.today()
usual="Made by Dimensional Blade."
oday=0


@client.event
async def on_ready():

  # bg_task.start()
  print('A new dimension unfurled and the letter A emerges')

@client.event
async def on_message(message):
  await helper.parseRoughWords(message)
  if message.author==client.user:
    return
  if message.content.startswith(data.prefix):
    await helper.parse_messages(message)


# @tasks.loop(seconds=14400)
# async def display_routine_everymorning():
#   timen = datetime.datetime.now().timetuple().tm_hour
#   if timen<8:
#     wday = datetime.datetime.now().wekday()
#     ch=client.get_channel(839145616529424384)
#     helper.display_routines(ch,data.days[wday])
#   '''
#   yo aaile paxi garxu aaile nai yettikai chodde
#   -lambe
#   untested codes are useless
#   '''
# @tasks.loop(seconds=14400)
# async def bg_task():
#   global oday

#   cha=client.get_channel(838611757857374228)
#   d=datetime.datetime.now().weekday()
#   if d!=oday:
#     await message.cha.send('Watever')
#     await helper.display_routines(data.days[2])
#     oday=d

    
#     print(oday)

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)



