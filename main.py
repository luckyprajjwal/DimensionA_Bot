import discord
import os
import datetime
from discord.ext import commands, tasks
from keepalive import keep_alive
import helper
import sqlprocess
import data


client = discord.Client()
#d=datetime.date.today()
usual="Made by Dimensional Blade."
oday=8


@client.event
async def on_ready():
  display_routine_everymorning.start()

  # bg_task.start()
  print('A new dimension unfurled and the letter A emerges')

@client.event
async def on_message(message):
  await helper.parseRoughWords(message)
  if message.author==client.user:
    return
  if message.content.startswith(data.prefix):
    await helper.parse_messages(message)
  elif message.content.startswith("```sql"):
    await sqlprocess.parseSQLQuery(message)


  


@tasks.loop(seconds=34400)
async def display_routine_everymorning():
  '''
  sup
  '''
  global oday
  wday = datetime.datetime.now().weekday()
  if wday!=oday:
    pass
    '''
    dherai choti garirathyo message 
    so cmt handeko ekxin lai 
    every run ma hanxa if disable garnu xa vane oday=wday condition ma haal mathi oday=0 haal github ma ekxoti push handinxu
    '''
    # oday=wday
    # ch=client.get_channel(839145616529424384)
    # await helper.display_routines(ch,data.days[wday])


my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)


