import discord
from discord.ext import commands
from core.classes import Cog_extension #從core/classes.py中引入Cor_extension類別
import random
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"延遲時間: {round(self.bot.latency * 1000, 2)}(ms)")

def setup(bot):
    bot.add_cog(Main(bot))#傳入bot物件從bot.py中取得設定檔
