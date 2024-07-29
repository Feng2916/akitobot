import discord
from discord import app_commands
from discord.ext import commands,tasks
import os
from itertools import cycle

bot=commands.Bot(command_prefix="%",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")
    activity = discord.Streaming(name="ULTRA C",url="https://www.youtube.com/watch?v=7WryveKlyX8")
    await bot.change_presence(status = discord.Status.idle, activity = activity)
    try:
        synced=await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="哈囉",description="讓彰人跟你說嗨")
async def hello(interaction:discord.Interaction):
    await interaction.response.send_message(f"よっ")

@bot.tree.command(name="ping",description="檢視機器人的延遲")
async def ping(interaction:discord.Interaction):
    ping_embed=discord.Embed(title="Ping",color=discord.Color.orange())
    ping_embed.add_field(name=f"{bot.user.name}的延遲：",value=f"{round(bot.latency*1000)}ms",inline=False)
    await interaction.response.send_message(embed=ping_embed,ephemeral=True)

bot.run("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")