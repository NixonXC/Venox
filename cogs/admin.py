import discord
from discord.ext import bridge, commands
import json
import sys
import os
import contextlib
import io

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(pass_context=True)
    @commands.is_owner()
    async def eval(self, ctx, *, code):
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        str_obj = io.StringIO()
        try:
            with contextlib.redirect_stdout(str_obj):
                exec(code)
        except Exception as e:
            return await send(f"```{e.__class__.__name__}: {e}```")
        await send(f'```{str_obj.getvalue()}```')

    @bridge.bridge_command(pass_context=True)
    @commands.is_owner()
    async def prefix(self, ctx, *, prefix):
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        with open('db/database.json', 'r') as f:
            config = json.load(f)
        config['PREFIX'] = prefix
        with open('db/database.json', 'w') as f:
            json.dump(config, f, indent=4)
        unup = config['PREFIX']
        await send(f"**Prefix changed to `{prefix}` | You will need to restart the bot for it to take effect.**")

def setup(bot):
  bot.add_cog(admin(bot))