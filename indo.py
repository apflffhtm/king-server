import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("KING서버봇이 성공적으로 켜졌습니다")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("KING 봇 일하는중"))

@client.event
async def on_message(message):
    if message.content.startswith ("킹 공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(826245593915588619)
            embed = discord.Embed(title="**KING서버 공지사항*", description="공지사항 내용은 항상 숙지 해주시기 바랍니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith ("킹 경고"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(826245595664482342)
            embed = discord.Embed(title="**KING서버 경고내역*", description="경고내역입니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 경고가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith ("킹 제재"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(826245595664482341)
            embed = discord.Embed(title="**KING서버 제재내역*", description="제재내역입니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 제재내역이 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith ("킹 이벤트"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(826245593915588621)
            embed = discord.Embed(title="**KING서버 이벤트 공지*", description="이벤트 공지입니다\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("**[ BOT 자동 알림 ]** | 정상적으로 이벤트 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

    if message.content.startswith ("KING청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text=" ", icon_url="https://cdn.discordapp.com/attachments/820496913991335966/831523872029409300/creation-logo-king-crown-esport_177315-133.jpg")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODMxNTI0MDc3MjQ3OTIyMjY2.YHWfJA.zHB2l44xwIEKjP1P7cG9wB2Ld_E')