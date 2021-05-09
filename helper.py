import discord
import data
import datetime
import kecnotice
from game2048.game2048 import game2048

client = discord.Client()


  
async def parse_messages(mess):
  message_text = mess.content[1:]
  if message_text == 'help':
    await display_help(mess)
  if message_text == 'notice':
    await displayKecNotice(mess)
  elif message_text in data.abs_days:
    enum_week = datetime.datetime.now().weekday()
    day1 = data.days[(enum_week + data.abs_days[message_text]) % 7]
    await display_routines(mess.channel, day1)

  elif message_text in data.days:
    await display_routines(mess.channel,message_text)
  else:
    await mess.channel.send(f"> Type `{data.prefix}help` for available commands")


async def display_routines(chan, day):
  # display_routines ( channel , day_of_week)
  # channel is the channel to send the data to obtained from a message as message.channel
  if day == 'saturday':
      await chan.send(file=discord.File('media/sanibar.jpg'))
      return
  if day == 'sunday':
      await chan.send(file=discord.File('media/sun.jpg'))
      return

  # Actual routine embed start here
  emb = discord.Embed(
      title=day.title(), description='', color=discord.Color.blurple())

  rout_classes = data.routines[day]
  for clas in rout_classes:
      emb.add_field(name=rout_classes[clas], value=clas, inline=False)
  emb.set_footer(text=f"\nMade by lambe")
  await chan.send(embed=emb)

async def display_routines(day):
  # display_routines ( channel , day_of_week)
  # channel is the channel to send the data to obtained from a message as message.channel
  global client
  chan=client.get_channel(838611757857374228)
  if day == 'saturday':
      await chan.send(file=discord.File('media/sanibar.jpg'))
      return
  if day == 'sunday':
      await chan.send(file=discord.File('media/sun.jpg'))
      return

  # Actual routine embed start here
  emb = discord.Embed(
      title=day.title(), description='', color=discord.Color.blurple())

  rout_classes = data.routines[day]
  for clas in rout_classes:
      emb.add_field(name=rout_classes[clas], value=clas, inline=False)
  emb.set_footer(text=f"\nMade by lambe")
  await chan.send(embed=emb)

async def parseRoughWords(msg):
  phrase = msg.content.lower().replace(" ", '')
  for i in data.roughWords:
      if i in phrase:
          await msg.channel.send('> Oe Mukh Nachad, terai ghar aayera thokdieula ni pheri')

async def display_help(messag):
  hstr = data.help_str
  emb = discord.Embed(title=f"Prefix Used : {data.prefix}")

  for each_cmd in hstr:
    # tit = each_cmd['title']
    tit = hstr[each_cmd]['title']
    de = f"{hstr[each_cmd]['desc']} \n ```php\n#Example of this command\n{hstr[each_cmd]['example']}```"
    emb.add_field(name=tit,value=de,inline=False)
  emb.set_footer(text=f"\nMade by lambe")
  await messag.channel.send(embed=emb)

async def displayKecNotice(mess):
  x = kecnotice.get_image_links(kecnotice.get_notice_urls(kecnotice.kec))
  for i in x:
    await mess.channel.send(embed=discord.Embed().set_image(url=i))
  

#2048 game implementation starts here


async def display_board(messag):
  pass
