import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online")
    
    @commands.command()
    async def ping(self,ctx):
        ping_embed=discord.Embed(title="Ping",color=discord.Color.orange())
        ping_embed.add_field(name=f"{self.bot.user.name}的延遲：",value=f"{round(self.bot.latency*1000)}ms",inline=False)
        await ctx.send(embed=ping_embed)

async def setup(bot):
    await bot.add_cog(Test(bot))