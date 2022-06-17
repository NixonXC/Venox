import discord
from discord.ext import bridge, commands
import json

with open('db/database.json', 'r') as f:
    config = json.load(f)

PREFIX = config['PREFIX']
AUTHOR = config['AUTHOR']

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(pass_context=True)
    async def ping(self, ctx: bridge.BridgeContext):
        """Returns the bot's latency."""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        em = discord.Embed(title="Pong! In",description=f"`{round(self.bot.latency * 1000)}`**ms**", color=discord.Colour.blurple())
        await send(embed=em)

    @bridge.bridge_command(pass_context=True)
    async def invite(self, ctx: bridge.BridgeContext):
        """Returns the bot's invite link."""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        em = discord.Embed(title="Invite Link", description=f"**[Click Here](https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions=8&scope=bot%20applications.commands)**", color=discord.Colour.blurple())
        await send(embed=em)

    @bridge.bridge_command(pass_context=True)
    async def github(self, ctx: bridge.BridgeContext):
        """Returns the bot's github link/source code."""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        em = discord.Embed(title="Github Link",description=f"**[Click Here](https://github.com/NixonXC/Veno-bot)**", color=discord.Colour.blurple())
        await send(embed=em)

    @bridge.bridge_command(pass_context=True)
    async def website(self, ctx: bridge.BridgeContext):
        """Official Website"""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        em = discord.Embed(title="Website Link",description=f"**[Click Here](https://venoxbot.tk/)**", color=discord.Colour.blurple())
        await send(embed=em)

    @bridge.bridge_command(pass_context=True)
    async def help(self, ctx):
        """Returns the help menu."""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        em = discord.Embed(title='Help:', description=f'**List of all the commands | prefix: `{PREFIX}`**', color=discord.Colour.blurple())
        em.add_field(name=f'Bot', value="`ping` , `eval <code>` , `prefix <prefix>` , `help`", inline=False)
        em.add_field(name=f'Links', value="`invite` , `website` , `github`", inline=False)
        em.add_field(name=f'Tools', value="`finder <user>` , `ipwhois <ip>` , `whois <domain>` , `phonewhois` , `checkemail <email>` , `nameservers <domain>` , `domainage <domain>`", inline=False)
        em.set_footer(text=f"This Bot is Made by {AUTHOR} for educational purposes")
        em.set_thumbnail(url="https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356")
        await send(embed=em)

def setup(bot):
  bot.add_cog(help(bot))