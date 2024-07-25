import discord
from discord.ext import commands

client=commands.Bot(command_prefix=">",intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")

@client.command()
async def hi(ctx):
    await ctx.send("よっ")

client.run("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")