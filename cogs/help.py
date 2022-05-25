import discord
from discord.ext import bridge, commands

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
        await send(f"**PING:** `{round(self.bot.latency * 1000)}`**ms**")

    @bridge.bridge_command(pass_context=True)
    async def help(self, ctx):
        """Returns the help menu."""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        em = discord.Embed(title='Help:', description='**List of all the commands | prefix: `a!`**', color=discord.Colour.blurple())
        em.add_field(name='`help`', value='Returns this message.', inline=False)
        em.add_field(name='`ping`', value='Returns the bot\'s latency.', inline=False)
        em.add_field(name='`finder <name>`', value='Finds accounts for the given account name.', inline=False)
        em.add_field(name='`ipwhois <ip>`', value='Returns information about the given IP address.', inline=False)
        em.add_field(name='`whois <domain>`', value='Returns the information about the  given domain.', inline=False)
        em.add_field(name="`phonewhois <phone-number>`", value="Returns information about the given phone number.", inline=False)
        em.set_footer(text="This Bot is Made by NixonXC for educational purposes")
        em.set_thumbnail(url="https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356")
        await send(embed=em)

def setup(bot):
  bot.add_cog(help(bot))