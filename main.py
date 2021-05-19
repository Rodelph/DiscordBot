import discord
from discord.ext import commands
import time
import random

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print('Bot is deployed !')

@client.event
async def on_member_join(member):
    guild = client.get_guild(647165695209111553)
    channel = guild.get_channel(647165695640993793)
    await channel.send(f'Welcome to this hot mess of a server {member.mention} ! :partying_face:')

@client.event
async def on_member_remove(member):
    guild = client.get_guild(647165695209111553)
    channel = guild.get_channel(647165695640993793)
    await channel.send(f'Had khona jraw 3lih {member.mention} ! :partying_face:')

@client.event
async def on_message(message):
    if message.author.id != 711018227940982794:
        if message.content.lower().startswith("hello"):
            await message.channel.send("Welcome welcome my friend :)")

        if message.content.lower().startswith("hi"):
            await message.channel.send("Welcome welcome my friend :)")

        if message.content.lower().startswith("yo"):
            await message.channel.send("Welcome welcome my friend :)")

        if message.content.lower().startswith("hhh"):
            await message.channel.send("HHHHHHHHHHHH")

        badwordsFile = './files/badwords.txt'
        bands = list()
        with open(badwordsFile) as bad:
            for line in bad:
                bands.append(line.strip())

        if any(word in message.content.lower() for word in bands):
            await message.channel.send("Jm3 rassek baraka man takhssar lhadra !")

    await client.process_commands(message)

@client.command()
async def ping(ctx):
    await ctx.send('Ping your #@* :D')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    resp_file = './files/8ball_responses.txt'
    bands = list()
    with open(resp_file) as resp:
        for line in resp:
            bands.append(line.strip())

    await ctx.send(f'Question: {question}\nAnswer: {bands[random.randint(0,7)]}')

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def nokta(ctx):
    noukat_file = './files/nokat.txt'
    bands = list()
    with open(noukat_file) as fin:
        for line in fin:
            bands.append(line.strip())

    await ctx.send(bands[random.randint(0,39)])

@client.command()
async def riddle(ctx):
    riddle_file = './files/qest_riddle.txt'
    bandsQuest = list()

    with open(riddle_file) as rid:
        for line in rid:
            bandsQuest.append(line.strip())

    riddle_file_Ans = './files/ans_riddle.txt'
    bandsAns = list()

    with open(riddle_file_Ans) as ridAns:
        for line in ridAns:
            bandsAns.append(line.strip())

    random_gen = random.randint(0,18)
    await  ctx.send(bandsQuest[random_gen])
    await  ctx.send("\n\nThe answer will be revealed after 15 seconds !\n")
    time.sleep(15.0)
    await ctx.send(bandsAns[random_gen])

@client.group(invoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title="Help", description="Use !help to show a list of every command that exists ! For more "
                                                 "information about the other commands please type !help "
                                                 "<name of the command>", color = 0xff0000)
    em.add_field(name= "4Fun", value="8ball, nokta, riddle")
    em.add_field(name="Moderation", value="clear, ban, kick, warn")
    await ctx.send(embed=em)

@help.command()
async def clear(ctx):
    em = discord.Embed(title="Clear", description="Clears the number of lines that the user desires to clear. If no "
                                                  "line number was selected, 2 lines will be cleared by default. "
                       , color = 0xF0F016)
    em.add_field(name="Syntax", value = "!clear <number of line>", inline=True)
    await ctx.send(embed=em)

@help.command()
async def riddle(ctx):
    em = discord.Embed(title="Riddle", description="The bot will give you a riddle, and after 15 seconds he shows the "
                                                   "answer !", color = 0x1CE134)
    em.add_field(name="Syntax", value= "!riddle", inline=True)
    await ctx.send(embed=em)

@help.command()
async def nokta(ctx):
    em = discord.Embed(title="Nokta", description="The bot will tell you a joke... (Some jokes are honestly meh, "
                                                  "but others are lit. It's just a coinflip :D)", color=0xB816F0)
    em.add_field(name = "Syntax", value="!riddle", inline=True)
    await ctx.send(embed=em)

@help.command(aliases=['8ball'])
async def _8ball(ctx):
    em = discord.Embed(title="8ball", description="You can ask the bot a question and he will answer you (Alert some "
                                                  "answers can be spicy !!)", color=0x1C7EE1)
    em.add_field(name = "Syntax", value = "!8ball", inline=True)
    await ctx.send(embed=em)

client.run('NzExMDE4MjI3OTQwOTgyNzk0.Xr85Uw.-X0fPl9oEPaiH-EgXpO1jQ7S9R4')
