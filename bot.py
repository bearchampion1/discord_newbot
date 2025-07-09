import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata = json.load(jfile)
    
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
    channel = bot.get_channel(int(jdata["Welcome_Channel_ID"]))#從json檔中讀取歡迎頻道ID(json檔回傳的是字串，所以要轉成int)
    await channel.send(f"歡迎 {member.mention} 來到伺服器！")#用await是因為協成
@bot.command() #指令
async def ping(ctx): #ctx是上下文 ex: A:嗨 (使用者,id,所在伺服器,所在頻道) B:早安
    await ctx.send(f"延遲時間:{round(bot.latency*1000,2)}(ms)") #bot.latency是bot的延遲時間，ctx.send是發送訊息到頻道
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Leave_Channel_ID"]))
    await channel.send(f"{member.mention} 離開伺服器！")#用await是因為協成
bot.run(jdata['TOKEN'])#bot啟動，並在括弧中填入token
#如果他不是loop執行完會閃退