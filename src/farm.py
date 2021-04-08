import discord
import time
from discord.ext.commands import Bot
from discord.ext import commands 
import asyncio 
from datetime import datetime
import random
import os

try:
    os.system("cls")
except:
    pass

print()
print("\033[35m███████\033[0m╗ \033[35m█████\033[0m╗ \033[35m██████\033[0m╗ \033[35m███\033[0m╗   \033[35m███\033[0m╗")
print("\033[35m██\033[0m════╝ \033[35m██\033[0m╔══\033[35m██\033[0m╗\033[35m██\033[0m╔══\033[35m██\033[0m╗\033[35m████\033[0m╗ \033[35m████\033[0m║")
print("\033[35m█████\033[0m╗  \033[35m███████\033[0m║\033[35m██████\033[0m╔╝\033[35m██\033[0m╔\033[35m████\033[0m╔\033[35m██\033[0m║")
print("\033[35m██\033[0m╔══╝  \033[35m██\033[0m╔══\033[35m██\033[0m║\033[35m██\033[0m╔══\033[35m██\033[0m╗\033[35m██\033[0m║╚\033[35m██\033[0m╔╝\033[35m██\033[0m║")
print("\033[35m██\033[0m║     \033[35m██\033[0m║  \033[35m██\033[0m║\033[35m██\033[0m║  \033[35m██\033[0m║\033[35m██\033[0m║ ╚═╝ \033[35m██\033[0m║")
print("")

print("\033[37m" + "Селфбот фармер для дискорда!")
print("\033[37mСделал ItsKek\n")

TOKEN = input("\033[33mТВОЙ TOKEN: ")

client = discord.Client()
b = Bot(command_prefix = "")

@b.event 
async def on_ready(): 
    print("\033[32mУспешный вход! Можете вводить команды которые сверху") 
print('''
\033[96m===============
\033[96mВерсия : 2.8.2
\033[96mПрефикс: *НЕТУ [Все команды без префикса]*
\033[96m===============
''')
print('''
\033[35m===========================================================
\033[96mЛИСТ КОМАНД
\033[96m[У ВСЕХ КОМАНД ЕСТЬ АНТИБАН]
\033[96mbrawl - фарм ОБЫЧНЫХ ящиков в боте BrawlBox
\033[96mbrawlM - фарм МЕГА ящиков в боте BrawlBox
\033[96mbrawlB - фарм БОЛЬШИХ ящиков в боте BrawlBox
\033[96mmine - фарм в IdleMiner
\033[96mdisboard - фарм бампов в disboard
\033[96mender - фарм в EnberBot
\033[96mworkAll - работа в UnbelievaBoat
\033[96m[Прописывает команды - !work, !crime, !slut, !depall]
\033[96mwork - работа в UnbelievaBoat
\033[96m[Прописывает команды - !work, !depall]
\033[35m============================================================
''')

@b.event 
async def on_message(message):

    if message.content == "mine":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начало фарма в Idle Miner... (Используется префикс ;) \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 1800

        while True:

            # anti ban
            tempsN = 60
            add = random.randint(2,7)
            temps = (tempsN + add)
    
            mtn3 = time.time()

            if mtn3 > mtn2:
                await message.channel.send(";rebirth")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Попытался сделать ребитх")
                mtn2 = mtn2 + 1800

            await message.channel.send(";s")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Продал вещи")
            time.sleep(1)
            await message.channel.send(";hunt")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[33m[{current_time}]: Запустил охоту")
            time.sleep(temps)                              #1m
            await message.channel.send(";s")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Продал вещи")
            time.sleep(temps)                              #1m
            await message.channel.send(";up p max")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[34m[{current_time}]: Прокачал кирку ")
            time.sleep(temps)                              #1m
            await message.channel.send(";s ")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Продал вещи")
            time.sleep(temps)                              #1m
            await message.channel.send(";s")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Продал вещи")
            time.sleep(temps)                              #1m
            await message.channel.send(";up b max")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[34m[{current_time}]: Прокочал рюкзак ")
            time.sleep(temps)

    if message.content == "brawl":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начало фарма в BrawlBox используя обычные ящики... \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 5

        while True:

            # anti ban
            tempsN = 1
            add = random.randint(1,2)
            temps = (tempsN + add)
    
            mtn3 = time.time()

            if mtn3 > mtn2:
                await message.channel.send("-b")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Открыл обычный ящик")
                mtn2 = mtn2 + 5

            await message.channel.send("-b")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Открыл обычный ящик")
            time.sleep(temps)                              #1m

    if message.content == "brawlB":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начало фарма в BrawlBox используя большие ящики... \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 5

        while True:

            # anti ban
            tempsN = 1
            add = random.randint(1,2)
            temps = (tempsN + add)
    
            mtn3 = time.time()

            if mtn3 > mtn2:
                await message.channel.send("-b")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Открыл большой ящик")
                mtn2 = mtn2 + 5

            await message.channel.send("-b")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Открыл большой ящик")
            time.sleep(temps)

    if message.content == "brawlM":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начало фарма в BrawlBox используя мега ящики... \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 5

        while True:

            # anti ban
            tempsN = 1
            add = random.randint(1,2)
            temps = (tempsN + add)
    
            mtn3 = time.time()

            if mtn3 > mtn2:
                await message.channel.send("-b")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Открыл мега ящик")
                mtn2 = mtn2 + 5

            await message.channel.send("-b")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\033[0m[{current_time}]: Открыл мега ящик")
            time.sleep(temps)

    if message.content == "ender":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Запуск фарма в EnderBot... \n")

        mtn1 = time.time()
        mtn2 = mtn1 + 3600
        mtn11 = time.time()
        mtn22 = mtn11 + 86400

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.channel.send(">hourly")
        print(f"\033[34m[{current_time}]: Получил часовую награду")
        time.sleep(2)
        await message.channel.send(">mine all")
        print(f"\033[34m[{current_time}]: Выкопал все")
        await message.channel.send(">daily")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\033[31m[{current_time}]: Получил дневную награду")

        while True:
            mtn3 = time.time()
            mtn33 = time.time()

            if mtn3 > mtn2:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                await message.channel.send(">hourly")
                print(f"\033[34m[{current_time}]: Получил часовую награду")
                time.sleep(2)
                await message.channel.send(">mine all")
                print(f"\033[34m[{current_time}]: Выкопал все")
                mtn2 = mtn2 + 3600

            if mtn33 > mtn22:
                await message.channel.send(">daily")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"\033[31m[{current_time}]: Получил дневную награду")
                mtn2 = mtn2 + 86400

            time.sleep(60)


    cmdinutile = ["!lb", "!top", "!help", "!rob", "!roulette 100 red", "!leadrboard", "!help", "!lb -bank", "!bal", "!money"]
    # random.choice(cmdinutile)

    if message.content == ('work'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начинаю фарм в Unbelievaboat... \n")

        while True:

            # anti ban
            tempsN = 300
            add = random.randint(7,15)
            temps = (tempsN + add)

            await message.channel.send("!work")
            time.sleep(1)
            await message.channel.send("!dep all")  
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: заработал ")
            print(f"\033[33m[{current_time}]: dep all ")
            time.sleep(temps)

    if message.content == ('workAll'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начинаю полную работу в Unbelievaboat... \n")

        while True:

            # anti ban
            tempsN = 300
            add = random.randint(7,15)
            temps = (tempsN + add)

            await message.channel.send("!work")
            time.sleep(1)
            await message.channel.send("!crime")
            time.sleep(1)
            await message.channel.send("!slut")
            time.sleep(1)
            await message.channel.send("!dep all")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Написал !work ")
            print(f"\033[34m[{current_time}]: Написал !crime ")
            print(f"\033[34m[{current_time}]: Написал !slut ")
            print(f"\033[33m[{current_time}]: Написал !dep all ")
            time.sleep(temps)
            await message.channel.send("!work")
            time.sleep(1)
            await message.channel.send("!dep all")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Написал !work ")
            print(f"\033[33m[{current_time}]: Написал !dep all ")
            time.sleep(temps)
    
    if message.content == ('bump'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n[{current_time}:] Начинаю бампить в DISBOARD... \n")

        while True:
            # anti ban
            tempsN = 7200
            add = random.randint(10,20)
            temps = (tempsN + add)

            await message.channel.send("!d bump")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"[{current_time}]: Успешный бамп! ")
            time.sleep(temps)



b.run(TOKEN, bot = False)


