import discord
from discord.ext import commands,tasks
import os
import asyncio
from itertools import cycle

bot=commands.Bot(command_prefix="%",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")
    activity = discord.Streaming(name="ULTRA C",url="https://www.youtube.com/watch?v=7WryveKlyX8")
    await bot.change_presence(status = discord.Status.idle, activity = activity)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")

asyncio.run(main())