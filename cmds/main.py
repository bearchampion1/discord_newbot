import discord
from discord.ext import commands
from core.classes import Cog_extension #從core/classes.py中引入Cog_extension類別
import random
class Main(Cog_extension):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"延遲時間: {round(self.bot.latency * 1000, 2)}(ms)")

def setup(bot):
    bot.add_cog(Main(bot)) 
