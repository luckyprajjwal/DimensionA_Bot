import discord
import data
import datetime



async def parse_messages(mess):
  message_text = mess.content[1:]
  await parseRoughWords(mess)

  if message_text in data.abs_days:
    #abs_days refers to abstract days like bholi hijo 
    enum_week = datetime.datetime.now().weekday()
    day1 = data.days[(enum_week + data.abs_days[message_text]) % 7]
    await display_routines(mess.channel, day1)

  if message_text in data.days:
    await display_routines(mess.channel,message_text)


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
    emb.set_footer(text="\nMade by lambe")
    await chan.send(embed=emb)

async def parseRoughWords(msg):
    phrase = msg.content.lower().replace(" ", '')
    for i in data.roughWords:
        if i in phrase:
            await msg.channel.send('> Oe Mukh Nachad, terai ghar aayera thokdieula ni pheri')
            await msg.delete()