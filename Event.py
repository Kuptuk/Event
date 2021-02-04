import discord
from discord.ext import commands
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
import io
import asyncio
import datetime
import pymongo
import random
import math
import inspect

client = commands.Bot(command_prefix = 'K.', intents = discord.Intents.all())
client.remove_command('help')

mm = os.environ.get("Mongo")
tt = os.environ.get("TOKEN")

my_client = pymongo.MongoClient(mm)

my_feb = my_client.feb.feb
my_feb2 = my_client.feb.feb2

admins = [562561140786331650,414119169504575509,529044574660853761]

@client.event
async def on_ready():
  global k, date, mas, all_hearts, kitty, cost, bal_case, colors
  k = 0
  date = datetime.datetime.utcnow()
  mas = {}
  all_hearts = {'k':'❤️', 'o':'🧡', 'j':'💛', 'z':'💚', 'g':'💙'}
  bal_case = {'k':'7', 'o':'6', 'j':'5', 'z':'4', 'g':'3'}
  cost = {'k':'7 валентинок', 'o':'6 валентинок', 'j':'5 валентинок', 'z':'4 валентинки', 'g':'3 валентинки'}
  colors = {'k':(217, 51, 65), 'o':(247, 142, 17), 'j':(254, 202, 93), 'z':(121, 176, 93), 'g':(94, 172, 236)}
  kitty = ['<a:z_kitty:750259811211542529>', '<:kitty_happy:794203420843442177>', '<a:z_HyperNeko:749672679522566146>', '<a:z_bongocat:749673203659571240>', '<a:Nefik22:802488380880322560>', '<:fox:610352379748941824>', '<:KannaWave:630856439921115162>', '<:helen_surveillance:786284424210939905>', '<:Helen22:700222377694330940>', '<:hehe:758212651464523806>', '<:ops:798301138633359400>', '<a:remspin:749672740021338213>', '<a:Rainbow_Weeb:749672953586647200>', '<:RemVV:774246427500478496>', '<a:z_funnyhelen2:758212956332490782>', '<a:funnyhelen1:758212978570297395>', '<a:funnyhelen3:758212859464908810>', '<:excuseme:610352380885860382>', '<:Angelina:792721358274035722>', '<:whoop:758212790153642024>']
  
@client.event
async def on_message(message):
  global k, date, mas, all_hearts, kitty, cost, bal_case, colors
  id_channel_event = 791799591434584074
  if message.channel.id == id_channel_event:
    k += 1
    temp = mas.get(str(message.content))
    if not temp is None:
      mas.pop(str(message.content))
      if [i for i in my_feb.find({'id':message.author.id})] == []:
        my_feb.insert_one({'id':message.author.id, 'k':0, 'o':0, 'j':0, 'z':0, 'g':0, 'bal':0})
      my_feb.update_one({"id":message.author.id}, {"$inc": {temp: 1, 'bal':int(bal_case.get(temp))}})
      await message.channel.send(embed=discord.Embed(colour=0xfc71d4, description=f'{all_hearts.get(temp)} {message.author.mention} успешно забрал сидечко {kitty[random.randint(1,19)]}\nТеперь его баланс пополнился на {cost.get(temp)} {kitty[random.randint(1,19)]}'))
      
  if k >= 152 or str(datetime.datetime.utcnow()-date).split('.')[0]>='0:30:00':
    if k >= 152:
      k = 0
    else:
      date = datetime.datetime.utcnow()
    rand = random.randint(1,100)
    if rand<=5:
      kapcha = random.randint(1000000,9999999)
      flag = 'k'
    elif rand>5 and rand<=20:
      kapcha = random.randint(100000,999999)
      flag = 'o'
    elif rand>20 and rand<=40:
      kapcha = random.randint(10000,99999)
      flag = 'j'
    elif rand>40 and rand<=65:
      kapcha = random.randint(1000,9999)
      flag = 'z'
    elif rand>65:
      kapcha = random.randint(100,999)
      flag = 'g'
    mas[f'{kapcha}'] = flag
    response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/804450569736683580/804481836750471168/review.png', stream = True).content))
    idraw = ImageDraw.Draw(response)
    idraw.text((0 , 0), f'{kapcha}', colors.get(flag), font = ImageFont.truetype(r'./Gothic.ttf', size = 50))
    response.save('14feb.png')
    await client.get_channel(id_channel_event).send(content=f'Появилось {all_hearts.get(flag)} сидечко, стоимостью {cost.get(flag)} <:KannaWave:630856439921115162>\nСкорее вводи капчу, чтобы забрать его первым <:whoop:758212790153642024>', file = discord.File(fp = '14feb.png'))
  await client.process_commands(message)
  
@client.command()
async def inv(message):
  if [i for i in my_feb.find({'id':message.author.id})] == []:
    my_feb.insert_one({'id':message.author.id, 'k':0, 'o':0, 'j':0, 'z':0, 'g':0, 'bal':0})
  a = my_feb.find({"id":message.author.id})[0]
  k = f'0{a.get("k")}' if a.get("k")<=9 else a.get("k")
  o = f'0{a.get("o")}' if a.get("o")<=9 else a.get("o")
  j = f'0{a.get("j")}' if a.get("j")<=9 else a.get("j")
  z = f'0{a.get("z")}' if a.get("z")<=9 else a.get("z")
  g = f'0{a.get("g")}' if a.get("g")<=9 else a.get("g")
  embed = discord.Embed(colour=0xfc71d4, timestamp=datetime.datetime.utcnow(), title=f'Инвентарь сидечек {message.author.name}', description=f'❤️ — `{k}`   ─▄█▀█▄──▄███▄─\n🧡 — `{o}`   ▐█░██████████▌\n💛 — `{j}`   ─██▒█████████─\n💚 — `{z}`   ──▀████████▀──\n💙 — `{g}`   ─────▀██▀─────\nВалентинок всего: `{a.get("bal")}`')
  embed.set_thumbnail(url=message.author.avatar_url)
  await message.channel.send(embed=embed)
  
@client.command()
async def top(message):
  if [i for i in my_feb.find({'id':message.author.id})] == []:
    my_feb.insert_one({'id':message.author.id, 'k':0, 'o':0, 'j':0, 'z':0, 'g':0, 'bal':0})
  a = [i for i in my_feb.find().sort('bal')][::-1]
  s, k = '', 1
  for i in a[0:10]:
    if message.author.id == i['id']:
      s += f'```css\n[{k}. {message.author} — {i["bal"]}]```'
    else:
      member = await client.fetch_user(i['id'])
      s += f'`{k}.` {member} — {i["bal"]}\n'
    k += 1
  
  if not str(message.author) in s:
    try:
      s += f'*• вжух вжух \n• здесь тоже есть\n• любовнички <:ops:798301138633359400>*\n`{[i["id"] for i in a].index(message.author.id)+1}.` {message.author} — {my_feb.find({"id":message.author.id})[0]["bal"]}'
    except:
      s += f'*• вжух вжух \n• здесь тоже есть\n• любовнички <:ops:798301138633359400>*\n`{len(a)+1}.` {message.author} — 0'

  embed = discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0xfc71d4, title='Топ по валентинкам <:ops:798301138633359400>', description=s)
  embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
  embed.set_thumbnail(url=message.guild.icon_url)
  await message.channel.send(embed=embed)

@client.command()
async def i(message, *, kogo=None):
  if kogo is None:
    await message.channel.send(embed=discord.Embed(colour=0xfc71d4, description='**Чтобы указать свою вторую половинку, необходимо в команде `K.i` ответить на вопрос, кого (или что 😳) вы любите?\n`Например:` K.i Себя <:hihi:657655166430085139>**'))
  elif len(kogo) > 20:
    await message.channel.send(embed=discord.Embed(colour=0xfc71d4, description='**Имя вашей второй половинки не может состоять из более чем 20-ти символов 🥺**'))
  else:
    my_feb2.delete_one({"id":message.author.id})
    my_feb2.insert_one({"id":message.author.id, "kogo":kogo})
    await message.channel.send(embed=discord.Embed(colour=0xfc71d4, description='**Вторая половинка успешно указана <:super:774247425539964959>\nТеперь её можно будет увидеть в карточке `K.info` <:fox:610352379748941824>**'))

client.run(tt)
