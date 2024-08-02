import discord
from discord import app_commands
from typing import Optional
from discord.app_commands import Choice
from discord.ext import commands,tasks
import os
from itertools import cycle
import math

bot=commands.Bot(command_prefix="--",intents=discord.Intents.all())

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

@bot.tree.command(name="ping",description="檢視機器人的延遲")
async def ping(interaction:discord.Interaction):
    ping_embed=discord.Embed(title="Ping",color=discord.Color.orange())
    ping_embed.add_field(name=f"{bot.user.name}的延遲：",value=f"{round(bot.latency*1000)}ms",inline=False)
    await interaction.response.send_message(embed=ping_embed,ephemeral=True)

@bot.tree.command(name="transpt",description="換算不同體力下的單場pt")
@app_commands.describe(pt="換算前單場pt",x="換算前開幾火",y="欲換算為開幾火")
@app_commands.choices(
    x=[
        Choice(name="0",value=1),
        Choice(name="1",value=5),
        Choice(name="2",value=10),
        Choice(name="3",value=15),
        Choice(name="4",value=19),
        Choice(name="5",value=23),
        Choice(name="6",value=26),
        Choice(name="7",value=29),
        Choice(name="8",value=31),
        Choice(name="9",value=33),
        Choice(name="10",value=35),
    ],
    y=[
        Choice(name="0",value=1),
        Choice(name="1",value=5),
        Choice(name="2",value=10),
        Choice(name="3",value=15),
        Choice(name="4",value=19),
        Choice(name="5",value=23),
        Choice(name="6",value=26),
        Choice(name="7",value=29),
        Choice(name="8",value=31),
        Choice(name="9",value=33),
        Choice(name="10",value=35),
    ]
)
async def pt1(interaction:discord.Interaction,pt:int,x:Choice[int],y:Choice[int]):
    x=x.value
    y=y.value
    await interaction.response.send_message(f"換算後pt為{pt*(y/x)}")

@bot.tree.command(name="re-pt",description="估算投入特定資源可獲得的pt")
@app_commands.describe(x="開幾火",t="歌曲總秒數",pt="所選開火情況下單場pt",cs="投入水晶總數",l="投入大罐總數",s="投入小罐總數")
@app_commands.choices(
    x=[
        Choice(name="1",value=1),
        Choice(name="2",value=2),
        Choice(name="3",value=3),
        Choice(name="4",value=4),
        Choice(name="5",value=5),
        Choice(name="6",value=6),
        Choice(name="7",value=7),
        Choice(name="8",value=8),
        Choice(name="9",value=9),
        Choice(name="10",value=10),
    ]
)
async def pt2(interaction:discord.Interaction,x:int,t:int,pt:int,cs:int,l:int,s:int):
    await interaction.response.send_message(f"可獲得{round(math.floor((cs/10+l*10+s)/x)*pt)}pt\n"
                                            f"共需打{math.floor((cs/10+l*10+s)/x)}場\n"
                                            f"需時{math.floor((math.floor((cs/10+l*10+s)/x)*t)/3600)}小時{math.floor((math.floor((cs/10+l*10+s)/x)*t)%3600/60)}分鐘")

@bot.tree.command(name="pt-re",description="估算達到特定pt所需投入的資源")
@app_commands.describe(x="開幾火",pt="所選開火情況下單場pt",r="目前的pt",e="欲達到的pt")
@app_commands.choices(
    x=[
        Choice(name="1",value=1),
        Choice(name="2",value=2),
        Choice(name="3",value=3),
        Choice(name="4",value=4),
        Choice(name="5",value=5),
        Choice(name="6",value=6),
        Choice(name="7",value=7),
        Choice(name="8",value=8),
        Choice(name="9",value=9),
        Choice(name="10",value=10),
    ]
)
async def pt3(interaction:discord.Interaction,x:int,pt:int,r:int,e:int):
    await interaction.response.send_message(f"再打{(e-r)/pt}場可達到{e}pt\n"
                                            f"共需投入{((e-r)/pt)*x*10}水晶")

bot.run("MTI2NTkyMjIxODc4NjAyOTYwOA.GPOcUG.22lGnV8oYt9uxdh27ojraaWNciTZo1pIKPB7XE")