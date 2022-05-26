import discord
from discord.ext import bridge, commands
import json

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

def setup(bot):
  bot.add_cog(admin(bot))