import json
import discord
from discord.ext import commands
from core.classes import Cog_extension
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata1 = json.load(jfile)

class Event(Cog_extension):
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata1["Welcome_Channel_ID"]))#從json檔中讀取歡迎頻道ID(json檔回傳的是字串，所以要轉成int)
        await channel.send(f"歡迎 {member.mention} 來到伺服器！")#用await是因為協成
    
    @commands.Cog.listener()
    async def on_member_remove(self , member):
        channel = self.bot.get_channel(int(jdata1["Leave_Channel_ID"]))
        await channel.send(f"{member.mention} 離開伺服器！")#用await是因為協成
    @commands.Cog.listener()
    async def on_message(self, message):#當有訊息時觸發
        keyword =['你好','早安','午安','晚安']
        if message.content in keyword and message.author != self.bot.user:#如果訊息內容以apple結尾，且不是bot自己發的訊息
            #message.author != self.bot.user是為了避免bot回應自己的訊息 
            await message.channel.send('你好，這是apple')#message.channel.send是發送訊息到「提出指令頻道」

def setup(bot):
    bot.add_cog(Event(bot))#傳入bot物件從bot.py中取得設定檔進React class