import discord
from discord.channel import CategoryChannel
import config
import parserr
import igruha
import favicon
import vsetor

client = discord.Client()


def create_embed(color, image_url, url, name, platform, author_name, author_url):
    embed=discord.Embed(title=name, url=url, description=f'Раздается на платформе: {platform}', color=color)
    embed.set_image(url=image_url)
    embed.set_author(name=author_name, url=author_url)
    return embed







@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_voice_state_update(member, before, after):
    guild = member.guild
    if after.channel:
        if after.channel.id == 825093182668800041:
            channell = await guild.create_voice_channel(f'💎{member}', category=after.channel.category)
            await member.move_to(channell)
            await channell.set_permissions(member, manage_channels=True)
    if before.channel:
        if before.channel.category.id == 825101960230862881 and before.channel.id != 825093182668800041 and not before.channel.members:
            try:
                await before.channel.delete()
            except:
                pass


@client.event
async def on_message(message):
        parsed = []
        if message.author == client.user:
            return

#help
        if message.content.startswith('$help'):
            helpembed = discord.Embed(title='Помощь', color=0x800080)
            helpembed.add_field(name="Бесплатные раздачи", value='```$free```', inline=False)
            helpembed.add_field(name="Поиск игр", value='''```$igruha [название игры]```
            ```$vsetor [название игры]```''', inline=False)
            await message.channel.send(embed = helpembed)
        

#free
        if message.content.startswith('$free'):
            color = 0x808080
            embed=discord.Embed(title='Команды раздачи', description='```$epic``` ```$steam``` ```$gog``` ```$playstation```', color=color)
            await message.channel.send(embed=embed)

        if message.content.startswith('$epic') or message.content.startswith('$steam') or message.content.startswith('$gog') or message.content.startswith('$playstation'):
                    parsed = list(reversed(parserr.parse()))
#Epic games
        if message.content.startswith('$epic'): 
            for each in parsed:
                if each[0] == 'Epic Games':
                    embed = create_embed(0x808080, each[3], each[2], each[1], each[0], 'FreeSteam', 'https://freesteam.ru/')
                    await message.channel.send(embed=embed)

#Steam
        if message.content.startswith('$steam'): 
            for each in parsed:
                if each[0] == 'Steam':
                    embed = create_embed(0x4682B4, each[3], each[2], each[1], each[0], 'FreeSteam', 'https://freesteam.ru/')
                    await message.channel.send(embed=embed)

#GOG
        if message.content.startswith('$gog'): 
            for each in parsed:
                if each[0] == 'GOG':
                    embed = create_embed(0xFFFF00, each[3], each[2], each[1], each[0], 'FreeSteam', 'https://freesteam.ru/')
                    await message.channel.send(embed=embed)

#playstation
        if message.content.startswith('$playstation'): 
            for each in parsed:
                if each[0] == 'PlayStation':
                    embed = create_embed(0xABB6F9, each[3], each[2], each[1], each[0], 'FreeSteam', 'https://freesteam.ru/')
                    await message.channel.send(embed=embed)




#igruha
        if message.content.startswith('$igruha'):
            k = 1
            if k == 0: 
                splitedMessage = message.content.split(' ')
                if len(splitedMessage) > 1:
                    getGames = igruha.parse(message.content[8:]) #Получаем список игр
                    if getGames:
                        n = 1
                        color = 0xFFFF00 #цвет для сообщения
                        embed=discord.Embed(title=getGames[0][1], url=getGames[0][0], color=color) #Добавил изначальные параметры сообщения
                        embed.set_thumbnail(url=getGames[0][2])
                        embed.set_author(name="Torrent Igruha", url="https://s1.torrents-igruha.org/", icon_url=favicon.get("https://s1.torrents-igruha.org/")[0].url)

                        
                        for each in getGames[1:]:
                            embed.add_field(name=f'{n} - {each[1]}', value=each[0], inline=False)
                            n += 1
                        await message.channel.send(embed=embed)
                    else:
                        await message.channel.send(embed = discord.Embed(title='Ошибка', description='Такой игры не найдено', color=0xFF0000))
                else:
                    await message.channel.send(embed = discord.Embed(title='Ошибка', description='Напишите название искомой игры', color=0xFF0000))
            else:
                await message.channel.send(embed = discord.Embed(title='Предупреждение', description='Эта команда временно не работает', color=0xDCE529))        

#vsetor
        if message.content.startswith('$vsetor'): 
            splitedMessage = message.content.split(' ')
            if len(splitedMessage) > 1:
                getGames = vsetor.parse(message.content[8:]) #Получаем список игр
                if getGames:
                    n = 1
                    color = 0xFFFF00 #цвет для сообщения
                    embed=discord.Embed(title=getGames[0][1], url=getGames[0][0], color=color) #Добавил изначальные параметры сообщения
                    embed.set_thumbnail(url=getGames[0][2])
                    embed.set_author(name="Vsetor", url="https://n1.vsetors.org/", icon_url=favicon.get("https://n1.vsetors.org/")[0].url)

                    
                    for each in getGames[1:]:
                        embed.add_field(name=f'{n} - {each[1]}', value=each[0], inline=False)
                        n += 1
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send(embed = discord.Embed(title='Ошибка', description='Такой игры не найдено', color=0xFF0000))
            else:
                await message.channel.send(embed = discord.Embed(title='Ошибка', description='Напишите название искомой игры', color=0xFF0000))

client.run(config.KEY)