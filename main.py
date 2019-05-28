import discord
from discord.ext import commands

TOKEN = '$youTokenHere'

client = discord.Client()

bot = commands.Bot(command_prefix='!', description='A bot that hits you back')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)



@client.event
async def on_ready():
    print("I am Ready!!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        #await client.send(message.channel, "World")
        await message.channel.send("World!")

@client.event
async def on_dice(message):
    if message.author == client.user:
        return
    if message.content == "!":

        await message.channel.send("World!")

client.run(TOKEN)
