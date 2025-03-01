import discord
from discord.ext import commands
import traceback


class GaatoBot(commands.Bot):
    def __init__(self, token):
        self.token = token
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=')', intents=intents)
        self.load_cogs()

    def load_cogs(self):
        cogs = ['gaato_bot.cogs.Voice', 'gaato_bot.cogs.TeX']
        for cog in cogs:
            self.load_extension(cog)
            print(cog + 'をロードしました')

    async def on_ready(self):
        print('起動しました')
    
    async def on_message_edit(self, before, after):
        if before.content == after.content:
            return
        await self.on_message(after)

    # 起動用の補助関数です
    def run(self):
        try:
            self.loop.run_until_complete(self.start(self.token))
        except discord.LoginFailure:
            print('Discord Tokenが不正です')
        except KeyboardInterrupt:
            print('終了します')
            self.loop.run_until_complete(self.close())
        except:
            traceback.print_exc()
