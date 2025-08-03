
from discord.ext import commands
from core.classes import Cog_extension #從core/classes.py中引入Cog_extension類別

class Main(Cog_extension , name='Main'):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"延遲時間: {round(self.bot.latency * 1000, 2)}(ms)")
    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)  #清除訊息，num+1是因為要包含指令本身
def setup(bot):
    bot.add_cog(Main(bot)) 
