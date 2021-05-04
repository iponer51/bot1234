#библеотеки
import discord
import os
import sqlite3
from discord.ext import commands
import time
from asyncio import sleep
import random
import json
#интенты
intents = discord.Intents()
intents.members = True
intents.presences = True
discord.Intents.all()

def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix,intents = discord.Intents.all())
client.remove_command("help")




def get_launge(client, message):
    with open("laung.json", "r") as f:
        launge = json.load(f)

    return launge[str(message.guild.id)]


def get_caps(client, message):
    with open("anticaps.json", "r") as f:
        caps = json.load(f)

    return caps[str(message.guild.id)]
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

        prefixes[str(guild.id)] = '$'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    #launge

    with open("laung.json", "r") as f:
        launge = json.load(f)

        launge[str(guild.id)] = 'en'

    with open('laung.json', 'w') as f:
        json.dump(launge, f, indent=4)


    with open("anticaps.json", "r") as f:
        caps = json.load(f)

        caps[str(guild.id)] = 'False'

    with open('anticaps.json', 'w') as f:
        json.dump(caps, f, indent=4)





@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


    with open("laung.json", "r") as f:
        launge = json.load(f)

    launge.pop(str(guild.id))

    with open('laung.json', 'w') as f:
        json.dump(launge, f, indent=4)


    with open("anticaps.json", "r") as f:
        caps = json.load(f)

    caps.pop(str(guild.id))

    with open('anticaps.json', 'w') as f:
        json.dump(caps, f, indent=4)


@client.command()
async def antilink(ctx):

    with open('anticaps.json', 'r')as f:
        caps = json.load(f)

    pre = caps[str(ctx.guild.id)]

    if pre == "False":
        with open('anticaps.json', 'r')as f:
            caps = json.load(f)

        caps[str(ctx.guild.id)] = "True"

        with open('anticaps.json', 'w')as f:
            json.dump(caps, f, indent=4)

        await ctx.send("Теперь анти линк у вас работает")

    if pre == "True":
        with open('anticaps.json', 'r')as f:
            caps = json.load(f)

        caps[str(ctx.guild.id)] = "False"

        with open('anticaps.json', 'w')as f:
            json.dump(caps, f, indent=4)

        await ctx.send("Теперь анти линк у вас НЕРАБОТАЕТ")
    else:
        print("Ты еблан")

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r')as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w')as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def changelaunge(ctx,ruen=None):
    if ruen is None:
        await ctx.send("You didn't specify launge en/rus")
    else:
        if ruen == "en":
            with open('laung.json', 'r')as f:
                launge = json.load(f)

            launge[str(ctx.guild.id)] = ruen

            with open('laung.json', 'w')as f:
                json.dump(launge, f, indent=4)

            await ctx.send("You have chosen the language to _en_")
        if ruen == "rus":
            with open('laung.json', 'r')as f:
                launge = json.load(f)

            launge[str(ctx.guild.id)] = ruen

            with open('laung.json', 'w')as f:
                json.dump(launge, f, indent=4)

            await ctx.send("Язык был изменен на русский")



    await ctx.send(f"Prefix changed to {prefix}")





@client.command()
async def test(ctx):
    with open('laung.json', 'r')as f:
        launge = json.load(f)

    pre = launge[str(ctx.guild.id)]
    if pre == "en":
        await ctx.send("English")
    if pre == "rus":
        await ctx.send("русский блять")

@client.command()
async def getprefix(ctx):
    with open('prefixes.json', 'r')as f:
            prefixes = json.load(f)

            pre = prefixes[str(ctx.guild.id)]

    await ctx.channel.send(f"Prefix on this server is {pre}")

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == '<@!809843655472971824>' or message.content == '<@809843655472971824>':

        with open('prefixes.json', 'r')as f:
            prefixes = json.load(f)

        pre = prefixes[str(message.guild.id)]

        await message.channel.send(f"Prefix on this server is {pre}")


    if message.content.startswith('https://discord.gg'):
        with open('anticaps.json', 'r')as f:
            caps = json.load(f)

        pre = caps[str(message.guild.id)]

        if pre == "True":
            await message.delete()
            await message.channel.send(f'{message.author},Не кидайте ссылки на сервер.')
        if pre == "False":
            pass


@client.command(aliases=['пинг'])
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')



client.run('ODA5ODQzNjU1NDcyOTcxODI0.YCa_rQ.juBZM-MOaKXIbyEKMSeitrJarw0')
