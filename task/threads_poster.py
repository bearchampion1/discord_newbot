
import requests
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import asyncio
import json
from core.classes import Cog_extension
with open('other_use.json', 'r', encoding='utf-8') as jfile:
    jdata1 = json.load(jfile)
with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata2 = json.load(jfile)
check_interval = 10 # seconds 
latest_post_url = None 
class ThreadsPoster(Cog_extension, name='ThreadsPoster'):
    def __init__(self, bot):
        super().__init__(bot)
        self.post_latest_thread.start()
        
    def fetch_latest_post_url(self, username):
        url = f"https://www.threads.net/@{username}"
        headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" # 模擬瀏覽器的User-Agent
        }
        try:
            response = requests.get(url , headers=headers)
            response.raise_for_status() # 檢查請求是否成功
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for script in soup.find_all("script"):
                if 'props' in script.text and f'/@' + username + '/post/' in script.text:
                    text = script.text
                    start = text.find(f"/@{username}/post/")
                    if start != -1:
                        end = text.find('"', start)
                        if end != -1:
                            post_path = text[start:end]
                            full_url = f"https://www.threads.net{post_path}"
                            print(f"Found post: {full_url}")
                            return full_url
            print("No posts found in the page")
            return None
        except requests.RequestException as e:
            print(f"爬取錯誤: {e}")
            return None
    @tasks.loop(minutes=0, seconds=check_interval)
    async def post_latest_thread(self):
        global latest_post_url #global變數是用來在函數內部修改全域變數
        try:
            print("執行")
            new_post_url = self.fetch_latest_post_url(jdata1['threads_channel_name'])
            if new_post_url and new_post_url != latest_post_url:
                latest_post_url = new_post_url
                channel = self.bot.get_channel(int(jdata2['Welcome_Channel_ID'])) #從json檔中讀取歡迎頻道ID(json檔回傳的是字串，所以要轉成int)
                if channel:
                    await channel.send(f"📢 @{jdata1['threads_channel_name']} 發佈了新 Threads！\n{latest_post_url}")
                else:
                    print("無法找到頻道！")
        except Exception as e:
            print(f"發生錯誤: {e}")

    @post_latest_thread.before_loop #before_loop是用來在loop開始前執行的函數
    async def before_post_latest_thread(self): 
        await self.bot.wait_until_ready() #等待bot準備好，這樣就不會在bot還沒準備好的時候就開始執行loop

def setup(bot):
    bot.add_cog(ThreadsPoster(bot))            