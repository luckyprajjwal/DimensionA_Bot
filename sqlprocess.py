import requests

url = 'https://tpcg.tutorialspoint.com/tpcg.php'

myhead = {
  'Accept': '*/*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Content-Length': '642',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'DNT': '1',
  'Host': 'tpcg.tutorialspoint.com',
  'Origin': 'https://www.tutorialspoint.com',
  'Pragma': 'no-cache',
  'Referer': 'https://www.tutorialspoint.com/',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'sec-ch-ua-mobile': '?0',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.38 Safari/537.36'
}
async def parseSQLQuery(mess):
  code = mess.content[6:-3]
  pyload = {
    'lang': 'sqlite',
    'device': '',
    'code': code,
    'stdinput': '',
    'ext': 'sql',
    'compile': 0,
    'execute': 'sqlite3 database.sdb < main.sql',
    'mainfile': 'main.sql',
    'uid': 6700370
  }
  
  r = requests.post(url, data=pyload, headers=myhead)
  resp = r.text.split("<br>")[1].replace('|','\t|\t')
  await mess.channel.send(resp)





  