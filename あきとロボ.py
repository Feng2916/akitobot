import discord
from discord.ext import commands
import os
import asyncio

bot=commands.Bot(command_prefix="%",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")
        
asyncio.run(main())