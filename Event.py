import discord 
from discord.ext import commands
from discord.utils import get
import os
import pymongo
import inspect
import random
import datetime
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
import io

client = commands.Bot(command_prefix = 'secret', intents = discord.Intents.all())
client.remove_command('help')

mm = os.environ.get("Mongo")
tt = os.environ.get("TOKEN")

my_client = pymongo.MongoClient(mm)

my_feb = my_client.feb.feb
my_feb2 = my_client.feb.feb2

admins = [562561140786331650,414119169504575509,529044574660853761]

@client.event
async def on_ready():
  global k, date, mas, all_hearts, kitty, cost, bal_case, colors, masfal
  k = 0
  date = datetime.datetime.utcnow()
  mas, masfal = {}, {}
  all_hearts = {'k':'❤️', 'o':'🧡', 'j':'💛', 'z':'💜', 'g':'💙'}
  bal_case = {'k':'7', 'o':'6', 'j':'5', 'z':'4', 'g':'3'}
  cost = {'k':'7 валентинок', 'o':'6 валентинок', 'j':'5 валентинок', 'z':'4 валентинки', 'g':'3 валентинки'}
  colors = {'k':(217, 51, 65), 'o':(247, 142, 17), 'j':(254, 202, 93), 'z':(170, 142, 214), 'g':(94, 172, 236)}
  kitty = ['<a:z_kitty:750259811211542529>', '<:kitty_happy:794203420843442177>', '<a:z_HyperNeko:749672679522566146>', '<a:z_bongocat:749673203659571240>', '<a:Nefik22:802488380880322560>', '<:fox:610352379748941824>', '<:KannaWave:630856439921115162>', '<:helen_surveillance:786284424210939905>', '<:Helen22:700222377694330940>', '<:hehe:758212651464523806>', '<:ops:798301138633359400>', '<a:remspin:749672740021338213>', '<a:Rainbow_Weeb:749672953586647200>', '<:RemVV:774246427500478496>', '<a:z_funnyhelen2:758212956332490782>', '<a:funnyhelen1:758212978570297395>', '<a:funnyhelen3:758212859464908810>', '<:excuseme:610352380885860382>', '<:Angelina:792721358274035722>', '<:whoop:758212790153642024>']
  await client.get_channel(791799591434584074).send('```css\n[Данные обновлены, бот перезапущен].```')

"""@client.event
async def on_message(message):
  global k, date, mas, all_hearts, kitty, cost, bal_case, colors, masfal, id_channel_event
  id_channel_event = 678657683246809152
  if message.channel.id == id_channel_event:
    k += 1
    temp = mas.get(str(message.content))
    if not temp is None:
      mas.pop(str(message.content))
      if [i for i in my_feb.find({'id':message.author.id})] == []:
        my_feb.insert_one({'id':message.author.id, 'k':0, 'o':0, 'j':0, 'z':0, 'g':0, 'bal':0})
      my_feb.update_one({"id":message.author.id}, {"$inc": {temp: 1, 'bal':int(bal_case.get(temp))}})
      await message.channel.send(embed=discord.Embed(colour=0xfc71d4, description=f'{all_hearts.get(temp)} {message.author.mention} успешно забрал сидечко {kitty[random.randint(1,19)]}\nТеперь его баланс пополнился на {cost.get(temp)} {kitty[random.randint(1,19)]}'))
      
    temp = masfal.get(str(message.content))
    if not temp is None:
      masfal.pop(str(message.content))
      if [i for i in my_feb.find({'id':message.author.id})] == []:
        my_feb.insert_one({'id':message.author.id, 'k':0, 'o':0, 'j':0, 'z':0, 'g':0, 'bal':0})
      my_feb.update_one({"id":message.author.id}, {"$inc": {temp: -1, 'bal':int(bal_case.get(temp))*-1}})
      await message.channel.send(embed=discord.Embed(colour=0x000001, description=f'<:black_heart:807219883766710293> {message.author.mention} попался на фальшивую капчу <:Helen_PMS:806879093261336586>\nТеперь его баланс уменьшился на {cost.get(temp)} <:Helen_PMS:806879093261336586> <:Helen_PMS:806879093261336586> <:Helen_PMS:806879093261336586>\n෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴\n─═ڿڰۣڿ☻ڿڰۣڿ═─<:black_heart:807219883766710293>─═ڿڰۣڿ☻ڿڰۣڿ═─\n෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴<:black_heart:807219883766710293>෴').set_thumbnail(url='https://media.discordapp.net/attachments/791799591434584074/807219403259248690/1.png'))
      
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
  await client.process_commands(message)"""
  
@client.command()
async def inv(message):
  if [i for i in my_feb.find({'id':message.author.id})] == []:
    my_feb.insert_one({'id':message.author.id, 'k':0, 'o':0, 'j':0, 'z':0, 'g':0, 'bal':0})
  a = my_feb.find({"id":message.author.id})[0]
  k = a.get("k")
  o = a.get("o")
  j = a.get("j")
  z = a.get("z")
  g = a.get("g")
  embed = discord.Embed(colour=0xfc71d4, timestamp=datetime.datetime.utcnow(), title=f'Инвентарь сидечек {message.author.name}', description=f'─▄█▀█▄──▄███▄─   ❤️ — `{k}`\n▐█░██████████▌   🧡 — `{o}`\n─██▒█████████─   💛 — `{j}`\n──▀████████▀──   💜 — `{z}`\n─────▀██▀─────   💙 — `{g}`\nВалентинок всего: `{a.get("bal")}`')
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

@client.command()
async def fal(message):
  global masfal, id_channel_event
  if message.author.id in admins:
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
    masfal[f'{kapcha}'] = flag
    response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/804450569736683580/804481836750471168/review.png', stream = True).content))
    idraw = ImageDraw.Draw(response)
    idraw.text((0 , 0), f'{kapcha}', colors.get(flag), font = ImageFont.truetype(r'./Gothic.ttf', size = 50))
    response.save('14feb.png')
    await client.get_channel(id_channel_event).send(content=f'Появилось {all_hearts.get(flag)} сидечко, стоимостью {cost.get(flag)} <:KannaWave:630856439921115162>\nСкорее вводи капчу, чтобы забрать его первым <:whoop:758212790153642024>', file = discord.File(fp = '14feb.png'))
  
@client.command()
async def norm(message):
  global mas, id_channel_event
  if message.author.id in admins:
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
async def info(message, id = None):
    if id == 'badges':
      embed = discord.Embed(colour=discord.Colour(0x310000),timestamp=datetime.datetime.utcnow(),title=':clipboard: Обозначение значков v3.0.5')
      embed.add_field(name='Значки Staff:',value='<:owner:784812161959854120> Владельцу сервера.\n<:developer:785191301321719828> Людям, принявшим участие в разработке/улучшении персонального бота.\n🏆 Лучшему работнику на данный момент.',inline=False)
      embed.add_field(name='Пользовательские значки 1:',value='<:KC_bug_hunter:807347751641022486> Людям, нашедшим баги в боте <@656029229749764126> с последующим информированием разработчика <@414119169504575509> в личных сообщениях.\n`Примечание:` имея данный значок, открывается возможность быть приглашённым на закрытое BETA-тестирование нововведений бота. При замечании определённого бага несколькими пользователями, только первый получит значок.\n<:old:788850405308104765> Людям, которые внесли огромный вклад в развитие сервера.\n<:alliance:807310319852585051> Представителям союза каталога.\n<:helper:799908854795731004> Людям, которые оказывали помощь новичкам, отвечая на их различные вопросы в общем чате.\n`Примечание:` помните, что вы можете лишиться значка за проявленную халатность.\n<:secret:787360058328481812> Секретный значок.',inline=False)
      embed.add_field(name='Пользовательские значки 2:',value='<:Attentive:807347751700004926> Нашли определённые несостыковки в информационных сообщениях? Сообщите администрации проекта и получите значок за внимательность.\n`Примечание:` значок распространяется на пользователей, что нашли определённые несостыковки в конкретном случае первыми.\n<:puzzle:799908854783016960> Предложившим большое количество дельных идей.\n‼️ Подавшему большое количество жалоб.\n<:review:799908854812377098> Оставившему рецензию серверу на 3-х мониторингах.\n`Примечание:` **[здесь](https://server-discord.com/604636579545219072)** и **[здесь](https://discord-server.com/ru/604636579545219072)**.',inline=False)
      embed.add_field(name='Значки-метки:',value='<:booster:797134090594680942> Бустерам сервера.\n<:p1:811016319607504936> Партнёру 1-го уровня.\n<:p2:811016319234605107> Партнёру 2-го уровня.\n<:p3:811016319716950046> Партнёру 3-го уровня.\n<:pmax:811016319238406175> Партнёру уровня MAX.',inline=False)
      embed.add_field(name='Значки ивентов:',value='🍬 Выдаётся в новогоднюю ночь 2021 года за найденные пасхалки. Существует до 2022 года.\n❤️ Победителю ивента на день влюблённых. Существует до конца мая 2021 года.',inline=False)
      embed.add_field(name='Примечания:',value='• Значков всего без учёта кастомных: `15`.\n• Кастомный значок возможен в случае больших заслуг перед Каталогом, а так же за 2 ваших буста.\n• Значки выдаются автоматизированной системой. Это значит, что нет необходимости выпрашивать их у администрации сервера.',inline=False)
      embed.set_footer(text=f'По запросу {message.author.name}',icon_url=message.author.avatar_url)
      embed.set_thumbnail(url=message.guild.icon_url)
      await message.channel.send(embed=embed)
    else:
      if id is None or id == '-':
        id = str(message.author.id)
      global msgbots; global bag; global medal22; global souz; global help; global rm22; global ngl; global att; global ideas; global bang; global msgotz; global candys; global heart; global msgs
      global crown; global dev; global bag22; global medal; global allia; global help22; global rm; global ngl2; global att22; global id22; global bg22; global cotz; global candy; global heart22
      sp = ['key', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
      randch = random.randint(1,100)
      color = (255, 255, 255)
      try:
          async with message.typing():
            member = client.get_guild(604636579545219072).get_member(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
            mid = member.id

            avatar = requests.get(member.avatar_url, stream = True)
            avatar = Image.open(io.BytesIO(avatar.content))
            avatar = avatar.convert('RGBA')

            b = [role.id for role in member.roles]
            if 608994688078184478 in b and list(message.message.content)[-1] != '-':
              if randch == 1:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784744502048063499/glitch.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              elif mid == 713780299024039936:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/802574569457713152/test.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              elif mid == 735540766289690646:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/791799591434584074/807999354652327946/13.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              elif mid == 571006178444836875:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/807933906975719444/cardo4ka.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              else:
                response = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/806867010851962880/staff.png', stream = True).content))
                idraw = ImageDraw.Draw(response)
              dol, otd, flag = 'Не указана', 'Отдел не указан', False
              if mid == 414119169504575509:
                dol = 'Разработчик'
                otd = 'Административный отдел'
                flag = True
              elif 620955813850120192 in b:
                dol = 'Администратор'
                otd = 'Административный отдел'
              elif 800474182474268734 in b:
                dol = 'Главный Модератор'
                otd = 'Административный отдел'
              elif 686639786672652363 in b:
                dol = 'Глава отдела партнерства'
                otd = 'Отдел партнерства'
              elif 686639826308825089 in b:
                dol = 'Глава отдела творчества'
                otd = 'Отдел творчества'
              elif 608600358570295307 in b:
                dol = 'Пиар-менеджер'
                otd = 'Отдел партнерства'
              elif 609043489841479700 in b:
                dol = 'Дизайнер'
                otd = 'Отдел творчества'
              elif 677397817966198788 in b:
                dol = 'аперативник'
                otd = 'Отдел ОБТ "Модер"'
              idraw.text((365, 313), f'{otd}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((365, 353), f'Должность: {dol}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

              if str(mid) in msgs:
                for i in msgs.split('\n'):
                  a = i.split('|')
                  if a[0] == str(mid):
                    idraw.text((365, 393), f'В команде с {a[1]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                    break

              warnow = 0
              for item in my_warn_md.find():
                if item['id'] == mid:
                  warnow += 1
              idraw.text((145 , 453), f'Выговоров: {warnow}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            else:
              if randch == 1:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/784744502048063499/glitch.png', stream = True)
              elif mid == 357518684723478540:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/812249880084873216/card_moxxie1.png', stream = True)
              elif mid == 414119169504575509:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/812252851077382164/card_helya.png', stream = True)
              elif not member.premium_since is None:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867001330630676/booster.png', stream = True)
              elif 769916590686732319 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867007156518932/max.png', stream = True)
              elif 622501691107049502 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867009064927282/pr3.png', stream = True)
              elif 622501656591990784 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867005503176734/gold.png', stream = True)
              elif 688654966675603491 in b:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867012067917831/test_ivent.png', stream = True)
              else:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867004198748160/classical.png', stream = True)
              response = Image.open(io.BytesIO(response.content))
              idraw = ImageDraw.Draw(response)
              if 769916590686732319 in b or 622501691107049502 in b or 622501656591990784 in b or 688654966675603491 in b:
                idraw.text((365, 440), f'Дата последнего обновления:', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                if d.get(mid) is not None:
                  datet = d.get(mid).split('.')[0].split()[0].split('-')
                  datet2 = d.get(mid).split('.')[0].split()[1]
                  idraw.text((365, 480), f'{datet[2]} {sp[int(datet[1])]} {datet[0]} года в {datet2}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                else:
                  idraw.text((365, 480), f'Неизвестна', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                kolvo = dk.get(mid) if dk.get(mid) is not None else 0
                idraw.text((135, 440), f'Публикаций: {kolvo}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

              try:
                aktiv = requests.get(f'http://185.244.172.127/stats?user={mid}').text
              except:
                aktiv = '? сообщений|? минут'
              idraw.text((365, 360), f'Активность сегодня: {aktiv.split("|")[0]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((365, 400), f'Voice сегодня: {aktiv.split("|")[1]}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            prioritet = -1
            ppz = [100, 140, 180, 220, 260, 300, 340, 380, 420, 440, 480, 520, 560, 600, 640, 680, 720]
            avatar = avatar.resize((212, 212), Image.ANTIALIAS)
            response.paste(avatar, (118, 182))
            idraw.text((400, 163), f'{member}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
            a = str(member.created_at).split()[0].split('-')
            idraw.text((365 , 193), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            a2 = str(member.joined_at).split()[0].split('-')
            idraw.text((365, 233), f'Дата вступления: {a2[2]} {sp[int(a2[1])]} {a2[0]} года', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            warnow = 0
            for item in my_warn.find():
              if item['id'] == mid:
                warnow += 1
            idraw.text((100 , 413), f'Предупреждений: {warnow}', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
            
            mst = str(member.status)
            if mst == 'offline':
              st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799364014276608/work4_79.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              y_2021 = 168
            elif member.is_on_mobile():
              if mst == 'online':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784741708964560906/t1.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'idle':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784741713007869972/t2.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'dnd':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784741716804239370/t3.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              y_2021 = 163
            else:
              if mst == 'online':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799369160425502/work11.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'idle':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799375640494110/work12.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              elif mst == 'dnd':
                st = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/784799380418723850/work31.png', stream = True).content)).convert('RGBA').resize((40, 40), Image.ANTIALIAS)
              y_2021 = 168
            response.paste(st, (360, y_2021), st)

            #prioritetnostb
            net_zn = 0
            if mid == message.guild.owner.id:
              prioritet += 1
              response.paste(crown, (ppz[prioritet], 105), crown)
              net_zn += 1

            if str(mid) in msgbots:
              prioritet += 1
              response.paste(dev, (ppz[prioritet], 105), dev)
              net_zn += 1

            if str(mid) in bag:
              prioritet += 1
              response.paste(bag22, (ppz[prioritet], 105), bag22)
              net_zn += 1

            if str(mid) in medal22:
              prioritet += 1
              response.paste(medal, (ppz[prioritet], 105), medal)
              net_zn += 1

            if str(mid) in souz:
              prioritet += 1
              response.paste(allia, (ppz[prioritet], 105), allia)
              net_zn += 1

            if str(mid) in help:
              prioritet += 1
              response.paste(help22, (ppz[prioritet], 105), help22)
              net_zn += 1

            if str(mid) in rm22:
              prioritet += 1
              response.paste(rm, (ppz[prioritet], 105), rm)
              net_zn += 1

            if str(mid) in ngl:
              prioritet += 1
              response.paste(ngl2, (ppz[prioritet], 105), ngl2)
              net_zn += 1

            if str(mid) in att:
              prioritet += 1
              response.paste(att22, (ppz[prioritet], 105), att22)
              net_zn += 1

            if str(mid) in ideas:
              prioritet += 1
              response.paste(id22, (ppz[prioritet], 105), id22)
              net_zn += 1

            if str(mid) in bang:
              prioritet += 1
              response.paste(bg22, (ppz[prioritet], 105), bg22)
              net_zn += 1

            if str(mid) in msgotz:
              prioritet += 1
              response.paste(cotz, (ppz[prioritet], 105), cotz)
              net_zn += 1

            if 688654966675603491 in b or 622501656591990784 in b or 622501691107049502 in b or 769916590686732319 in b:
              if 688654966675603491 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015500712509490/6.png', stream = True).content)).convert('RGBA')
              elif 622501656591990784 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015502381187092/34.png', stream = True).content)).convert('RGBA')
              elif 622501691107049502 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015503648784424/41.png', stream = True).content)).convert('RGBA')
              elif 769916590686732319 in b:
                znpart = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/811015504348708914/52.png', stream = True).content)).convert('RGBA')
              prioritet += 1
              response.paste(znpart, (ppz[prioritet], 105), znpart)
              net_zn += 1

            if str(mid) in candys:
              prioritet += 1
              response.paste(candy, (ppz[prioritet], 105), candy)
              net_zn += 1

            if str(mid) in heart:
              prioritet += 1
              response.paste(heart22, (ppz[prioritet], 105), heart22)
              net_zn += 1

            if mid == 394757049893912577:
              fat = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/785202689532755988/fatal.png', stream = True).content)).convert('RGBA').resize((37, 37), Image.ANTIALIAS)
              response.paste(fat, (54, 100), fat)   
            elif mid == 713780299024039936:
              ang = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/797940366254800906/rm.png', stream = True).content)).convert('RGBA')
              response.paste(ang, (54, 100), ang)
            elif mid == 346263496394276867:
              nef = Image.open(io.BytesIO(requests.get('https://cdn.discordapp.com/attachments/682929799991132207/800773662453530644/review.png', stream = True).content)).convert('RGBA')
              response.paste(nef, (54, 100), nef)
            elif mid == 357518684723478540:
              mox = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/803224903620362260/review.png', stream = True).content)).convert('RGBA')
              response.paste(mox, (54, 100), mox)
            elif mid == 722394482515116072:
              gof = Image.open(io.BytesIO(requests.get('https://cdn.discordapp.com/attachments/682929799991132207/803001131185733632/review.png', stream = True).content)).convert('RGBA')
              response.paste(gof, (54, 100), gof)
            elif mid == 420506181627412501:
              rez = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/806622139972583485/review.png', stream = True).content)).convert('RGBA')
              response.paste(rez, (54, 100), rez)
            elif mid == 571006178444836875:
              leo = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/682929799991132207/799946949679120424/review.png', stream = True).content)).convert('RGBA')
              response.paste(leo, (54, 100), leo)

            if net_zn == 0:
              idraw.text((365 , 200), f'У вас пока нет ни одного значка ;(', color, font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

            if randch == 1:
              gl = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/786978327420076062/glitchon.png', stream = True).content)).convert('RGBA')
              response.paste(gl, (0, 0), gl)
              response.save('user_card.png')
              await message.channel.send(content='О̵͌́й̶̿̒.̵̅͛.̵̯̃.̶̊̿ ̵̇̚В̷̒̀ӹ̸́̈ ̸̍͝с̷͐͐л̷͒̊о̵͑̌м̶̐̿ӓ̶́͐л̸̒̍и̸͂̚ ̶͌͘б̶̍̾о̷̇̈́т̴̋̓а̶̎͊ ',file = discord.File(fp = 'user_card.png'))
            else:
              response.save('user_card.png')
              await message.channel.send(file = discord.File(fp = 'user_card.png'))

      except:
          try:
              randch = random.randint(1,100)
              member = await client.fetch_user(int(id.replace("!", "").replace("@","").replace("<","").replace(">","")))
              avatar = requests.get(member.avatar_url, stream = True)
              avatar = Image.open(io.BytesIO(avatar.content))
              avatar = avatar.convert('RGBA')
              if randch == 1:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/784744502048063499/glitch.png', stream = True)
              else:
                response = requests.get('https://media.discordapp.net/attachments/689800301468713106/806867004198748160/classical.png', stream = True)
              response = Image.open(io.BytesIO(response.content))
              idraw = ImageDraw.Draw(response)
              avatar = avatar.resize((212, 212), Image.ANTIALIAS)
              response.paste(avatar, (119, 171, 331, 383))
              a = str(member.created_at).split()[0].split('-')
              idraw.text((365, 150), f'{member}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 35))
              idraw.text((365, 220), f'Дата создания: {a[2]} {sp[int(a[1])]} {a[0]} года', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              idraw.text((95 , 440), 'Пользователь отсутствует на сервере. Функции ограничены.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
              try:
                a = await client.get_guild(604636579545219072).fetch_ban(member)
                idraw.text((365 , 260), 'Пользователь в бане.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))
                b_01 = [role.id for role in message.author.roles]
                if 677397817966198788 in b_01 or 765212719380037663 in b_01 or 800474182474268734 in b_01 or message.author.id in admins:
                  idraw.text((52 , 520), f'Причина: {a.reason}', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 20))
                else:
                  idraw.text((52 , 520), 'Просматривать причину бана могут лишь уполномоченные сотрудники.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 20))
              except:
                idraw.text((365 , 260), 'Пользователь не забанен.', (255, 255, 255), font = ImageFont.truetype(r'./Gothic.ttf', size = 25))

              if randch == 1:
                gl = Image.open(io.BytesIO(requests.get('https://media.discordapp.net/attachments/689800301468713106/786978327420076062/glitchon.png', stream = True).content)).convert('RGBA')
                response.paste(gl, (0, 0), gl)
                response.save('user_card.png')
                await message.channel.send(content='О̵͌́й̶̿̒.̵̅͛.̵̯̃.̶̊̿ ̵̇̚В̷̒̀ӹ̸́̈ ̸̍͝с̷͐͐л̷͒̊о̵͑̌м̶̐̿ӓ̶́͐л̸̒̍и̸͂̚ ̶͌͘б̶̍̾о̷̇̈́т̴̋̓а̶̎͊ ',file = discord.File(fp = 'user_card.png'))
              else:
                response.save('user_card.png')
                await message.channel.send(file = discord.File(fp = 'user_card.png'))
          except:
              await message.channel.send('```css\nПользователя не существует.```')

client.run(tt)
