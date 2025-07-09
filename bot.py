import discord
from discord.ext import commands
import json
import random
import os
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata1 = json.load(jfile)
with open('other_use.json', 'r', encoding='utf-8') as jfile:
    jdata2 = json.load(jfile)    
DISCORD_BOT_TOKEN = None #備用
intents = discord.Intents.default()
intents.members = True #啟用成員相關的事件
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event #bot底下的事件
async def on_ready():#async def 義務函數
    print(">> Bot is online <<")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata1["Welcome_Channel_ID"]))#從json檔中讀取歡迎頻道ID(json檔回傳的是字串，所以要轉成int)
    await channel.send(f"歡迎 {member.mention} 來到伺服器！")#用await是因為協成
    


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata1["Leave_Channel_ID"]))
    await channel.send(f"{member.mention} 離開伺服器！")#用await是因為協成


@bot.command() #指令
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}') #載入指令檔案，去掉.py的部分
    await ctx.send(f'load {extension} done!') #回傳訊息到提出指令頻道  
    
@bot.command() #指令
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}') #載入指令檔案，去掉.py的部分
    await ctx.send(f'un-loaded {extension} done!') #回傳訊息到提出指令頻道            

    
@bot.command() #指令
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}') #載入指令檔案，去掉.py的部分
    await ctx.send(f'Re-loaded {extension} done!') #回傳訊息到提出指令頻道                      
for filename in os.listdir('./cmds'): 
    if filename.endswith('.py'): #檢查檔案是否以.py結尾
        bot.load_extension(f'cmds.{filename[:-3]}') #載入指令檔案，去掉.py的部分
if __name__ == '__main__': #如果這個檔案是主程式
    bot.run(jdata1['TOKEN'])#bot啟動，並在括弧中填入token
#如果他不是loop執行完會閃退