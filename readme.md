
PREFIX USED = $



TO IMPLEMENT

-- Display next day when the class of a subject will occur
eg: 
```python
def next_class(message):
  # message content is like 'next EE'
  x = message.content.split(' ')
  subject = x[1]
  #subject can be codes like, 'COA' or 'EE' 'DBMS' 'CN' 
  # 'OS' 'FD'
  # now find when the next class and time that subject is
  #and just display the time as

  x =' Tuesday from xx:xx to xx:xx '
  await message.channel.send(f"> {x}")
  
```

-- TO DO:

-- Take in pdf from chat message above you  and watermark and return a watermarked pdf or images or zip file

-- Take in images, from chat messages above watermark them and return images or pdf  or zip as user likes

