import discord
from discord.ext import commands

bot=commands.Bot(command_prefix="%",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")

@bot.command(aliases=("hello","嗨","哈囉"))
async def hi(ctx):
    await ctx.send("よっ")

@bot.command()
async def ping(ctx):
    ping_embed=discord.Embed(title="Ping",color=discord.Color.orange())
    ping_embed.add_field(name=f"{bot.user.name}的延遲：",value=f"{round(bot.latency*1000)}ms",inline=False)
    await ctx.send(embed=ping_embed)

#with open("token.txt") as f:
#    token=f.read()

#bot.run(token)

bot.run("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")