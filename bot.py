import discord
from discord import app_commands
from typing import Optional
from discord.app_commands import Choice
from discord.ext import commands,tasks
import os
from itertools import cycle
import math

bot=commands.Bot(command_prefix="PREFIX",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready")
    activity = discord.Streaming(name="NAME",url="URL")
    await bot.change_presence(status = discord.Status.idle, activity = activity)
    try:
        synced=await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="help",description="查看あきとロボ指令表")
async def help(interaction:discord.Interaction):
    ping_embed=discord.Embed(title="あきとロボ指令一覽",color=discord.Color.orange())
    ping_embed.add_field(name=f"機器人故障請洽：",value=f"**_3823051904**",inline=False)
    ping_embed.add_field(name=f"**/help**",value=f"查看あきとロボ指令表",inline=False)
    ping_embed.add_field(name=f"**/transpt**",value=f"換算不同體力下的單場pt\n"
                         f"-# pt：換算前單場pt\n"
                         f"-# x：換算前開幾火\n"
                         f"-# y：欲換算為開幾火",inline=False)
    ping_embed.add_field(name=f"**/re-pt**",value=f"估算投入特定資源可獲得的pt\n"
                         f"-# x：開幾火\n"
                         f"-# t：歌曲總秒數(可參考https://sekai.best/music)\n"
                         f"-# pt：所選開火及歌曲情況下的單場pt\n"
                         f"-# cs：投入水晶總數\n"
                         f"-# l：投入大罐總數\n"
                         f"-# s：投入小罐總數",inline=False)
    ping_embed.add_field(name=f"**/pt-re**",value=f"估算達到特定pt所需投入的資源\n"
                         f"-# x：開幾火\n"
                         f"-# t：歌曲總秒數(可參考https://sekai.best/music)\n"
                         f"-# pt：所選開火及歌曲情況下的單場pt\n"
                         f"-# r：目前的pt\n"
                         f"-# e：欲達到的pt",inline=False)
    ping_embed.add_field(name=f"**/ccn**",value=f"令房號顯示於頻道名稱中\n"
                         f"-# r：房號",inline=False)
    ping_embed.add_field(name=f"**aktfw (5字母+1空格，這不是斜線指令)**",value=f"令募集訊息顯示在特定頻道中\n",inline=False)
    await interaction.response.send_message(embed=ping_embed)

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
    await interaction.response.send_message(f"換算後pt為{round(pt*(y/x))}")

@bot.tree.command(name="re-pt",description="估算投入特定資源可獲得的pt")
@app_commands.describe(x="開幾火",t="歌曲總秒數",pt="所選開火及歌曲情況下的單場pt",cs="投入水晶總數",l="投入大罐總數",s="投入小罐總數")
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
@app_commands.describe(x="開幾火",t="歌曲總秒數",pt="所選開火及歌曲情況下的單場pt",r="目前的pt",e="欲達到的pt")
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
async def pt3(interaction:discord.Interaction,x:int,t:int,pt:int,r:int,e:int):
    await interaction.response.send_message(f"再打{math.ceil((e-r)/pt)}場可達到{e}pt\n"
                                            f"共需投入{(math.ceil((e-r)/pt))*x*10}水晶\n"
                                            f"需時{math.floor((math.ceil((e-r)/pt)*t)/3600)}小時{math.floor(((math.ceil((e-r)/pt))*t)%3600/60)}分鐘")

@bot.tree.command(name="ccn",description="令房號顯示於頻道名稱中")
@app_commands.describe(r="房號")
async def rename(interaction:discord.Interaction,r:int):
    if 1<=r<=9:
        await interaction.channel.edit(name='0000'+str(r))
        await interaction.response.send_message(f"成功更改房號為**0000{r}**\n"
                                                f"-# 注意：由於速率限制，十分鐘內僅能使用該指令兩次")
    elif 10<=r<=99:
        await interaction.channel.edit(name='000'+str(r))
        await interaction.response.send_message(f"成功更改房號為**000{r}**\n"
                                                f"-# 注意：由於速率限制，十分鐘內僅能使用該指令兩次")
    elif 100<=r<=999:
        await interaction.channel.edit(name='00'+str(r))
        await interaction.response.send_message(f"成功更改房號為**00{r}**\n"
                                                f"-# 注意：由於速率限制，十分鐘內僅能使用該指令兩次")
    elif 1000<=r<=9999:
        await interaction.channel.edit(name='0'+str(r))
        await interaction.response.send_message(f"成功更改房號為**0{r}**\n"
                                                f"-# 注意：由於速率限制，十分鐘內僅能使用該指令兩次")
    elif 10000<=r<=99999:
        await interaction.channel.edit(name=r)
        await interaction.response.send_message(f"成功更改房號為**{r}**\n"
                                                f"-# 注意：由於速率限制，十分鐘內僅能使用該指令兩次")
    else:
        await interaction.channel.edit(name="00000_")
        await interaction.response.send_message(f"房號格式錯誤，已自動更改為預設頻道名稱\n"
                                                f"-# 注意：由於速率限制，十分鐘內僅能使用該指令兩次")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    words = ['aktfw ']
    TargetChannel=bot.get_channel(CHANNEL_ID)

    for word in words:
        if word in message.content and (message.channel.id==CHANNEL_ID or message.channel.id==CHANNEL_ID or message.channel.id==CHANNEL_ID or message.channel.id==CHANNEL_ID or message.channel.id==CHANNEL_ID):
            await TargetChannel.send(f"{message.content.replace('aktfw ', '🚗\n募車人：'+'<@'+str(message.author.id)+'>\n房間：<#'+str(message.channel.id)+'>\n\n')}")

    await bot.process_commands(message)

bot.run(TOKEN)
