import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json

with open('other_use.json', 'r', encoding='utf-8') as jfile:
    jdata2 = json.load(jfile)  # 從other_use.json讀取資料，並將其轉換為Python字典格式
class React(Cog_extension, name='react'):
    
    @commands.command() #指令
    async def 圖片(self ,ctx):#傳送圖片的指令區
        random_pic = random.choice(jdata2["pic1"])   #從json檔中隨機選擇一張圖片
        pic = discord.File(random_pic) #discord.File是discord.py中用來處理檔案的類別，括號中填入圖片的路徑 
        await ctx.send(file = pic)  #ctx.send是發送訊息到提出指令頻道，file是發送檔案 

    @commands.command()
    async def web_pic(self ,ctx):
        random_pic = random.cshoice(jdata2["web_pic"])   #從json檔中隨機選擇一張圖片 
        await ctx.send(random_pic)  #ctx.send是發送訊息到提出指令頻道，file是發送檔案

def setup(bot):
    bot.add_cog(React(bot))#傳入bot物件從bot.py中取得設定檔進React class