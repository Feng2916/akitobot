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
            await bot.load_extension(f"cog.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")

#@bot.command(aliases=("hello","嗨","哈囉"))
#async def hi(ctx):
#    await ctx.send("よっ")

#@bot.command()
#async def ping(ctx):
#    ping_embed=discord.Embed(title="Ping",color=discord.Color.orange())
#    ping_embed.add_field(name=f"{bot.user.name}的延遲：",value=f"{round(bot.latency*1000)}ms",inline=False)
#    await ctx.send(embed=ping_embed)

asyncio.run(main())