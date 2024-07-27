import discord
from discord.ext import commands,tasks
import os
import asyncio
from itertools import cycle

bot=commands.Bot(command_prefix="%",intents=discord.Intents.all())

bot_statuses=cycle(["プロセカ","プロセカ"])

@tasks.loop(seconds=60)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

@bot.event
async def on_ready():
    print("Bot ready")
    change_bot_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")

asyncio.run(main())