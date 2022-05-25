import discord
import aiohttp
from sqlalchemy import desc
import whois
import phonenumbers
from phonenumbers import geocoder, carrier
from discord.ext import bridge, commands
import re
from phonenumbers import timezone

nonsearch = ["192.168.1.1","127.0.0.1","69.69.69.69"]

async def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

gex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(gex, email)):
        return True
    else:
        return False

def urlify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '-', s)
    return s

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command()
    async def phonewhois(self, ctx, phone):
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        x = phonenumbers.parse(f"+{phone}", None)
        zone = timezone.time_zones_for_number(x)
        car = carrier.name_for_number(x, 'en')
        region = geocoder.description_for_number(x, 'en')
        valid = phonenumbers.is_valid_number(x)
        em = discord.Embed(title=f"Phone Number Info", color=discord.Colour.blurple())
        em.add_field(name="Phone Number", value=f"`{phone}`")
        em.add_field(name="Valid", value=f"`{valid}`", inline=False)
        try:
            em.add_field(name="Timezone", value=f"`{zone}`", inline=False)
        except:
            em.add_field(name="Timezone", value="`Unknown`", inline=False)
        try:
            em.add_field(name="Carrier", value=f"`{car}`", inline=False)
        except:
            em.add_field(name="Carrier", value="`Unknown`", inline=False)
        try:
            em.add_field(name="Region", value=f"`{region}`", inline=False)
        except:
            em.add_field(name="Region", value="`Unknown`", inline=False)
        em.set_footer(text="All this information can be found on the internet.")
        em.set_thumbnail(url=f'https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356')
        await send(embed=em)

    @bridge.bridge_command()
    async def ipwhois(self, ctx: bridge.BridgeContext, ip):
        """Returns Public information about the given IP address."""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        if ip in nonsearch:
            await send("**I cannot search that IP; maybe you're trying something suspicious.**")
            return
        else:
            ip_info = await get_ip_info(ip)
            em = discord.Embed(title=f"{ip}", color=discord.Colour.blurple())
            em.add_field(name="IP", value=f"`{ip_info['query']}`", inline=False)
            em.add_field(name="ISP", value=f"`{ip_info['isp']}`", inline=False)
            em.add_field(name="ASN", value=f"`{ip_info['as']}`", inline=False)
            em.add_field(name="Country", value=f"`{ip_info['country']}`", inline=False)
            em.add_field(name="Region", value=f"`{ip_info['regionName']}`", inline=False)
            em.add_field(name="City", value=f"`{ip_info['city']}`", inline=False)
            em.add_field(name="Zip", value=f"`{ip_info['zip']}`", inline=False)
            em.add_field(name="Timezone", value=f"`{ip_info['timezone']}`", inline=False)
            em.add_field(name="Latitude", value=f"`{ip_info['lat']}`", inline=False)
            em.add_field(name="Longitude", value=f"`{ip_info['lon']}`", inline=False)
            em.add_field(name="ISP", value=f"`{ip_info['isp']}`", inline=False)
            em.add_field(name="Organization", value=f"`{ip_info['org']}`", inline=False)
            em.add_field(name="Note", value=f"**ALL THIS INFORMATION IS PUBLIC AND AVAILABLE ON THE INTERNET**", inline=False)
            em.set_footer(text=f"THIS TOOL IS MADE FOR EDUCATIONAL PURPOSES ONLY")
            em.set_thumbnail(url=f'https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356')
            await send(embed=em)

    @bridge.bridge_command()
    async def whois(self, ctx: bridge.BridgeContext, domain):
        """Get the WHOIS information of a domain"""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        w = whois.whois(domain)
        dom = discord.Embed(title=f"{domain}", description="All The Found Public Info", color=discord.Colour.blurple())
        dom.add_field(name="Domain Name:", value=f"`{w.domain_name}`", inline=False)
        dom.add_field(name="Registrar:", value=f"`{w.registrar}`", inline=False)
        dom.add_field(name="Abuse Report Email:", value=f"`{w.emails}`", inline=False)
        dom.add_field(name="Name", value=f"`{w.name}`", inline=False)
        dom.add_field(name="Organization", value=f"`{w.org}`", inline=False)
        dom.add_field(name="Country", value=f"`{w.country}`", inline=False)
        dom.add_field(name="State", value=f"`{w.state}`", inline=False)
        dom.add_field(name="City", value=f"`{w.city}`", inline=False)
        dom.add_field(name="Address", value=f"`{w.address}`", inline=False)
        dom.add_field(name="Zipcode", value=f"`{w.zipcode}`", inline=False)
        dom.add_field(name="Created", value=f"`{w.creation_date}`", inline=False)
        dom.add_field(name="Expiration", value=f"`{w.expiration_date}`", inline=False)
        dom.add_field(name="Note", value=f"**ALL THIS INFORMATION IS PUBLIC AND AVAILABLE ON THE INTERNET** [Wikipedia WHOIS DATABASE](https://en.wikipedia.org/wiki/WHOIS)", inline=False)
        dom.set_footer(text=f"THIS TOOL IS MADE FOR EDUCATIONAL PURPOSES ONLY")
        dom.set_thumbnail(url=f'https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356')
        await send(embed=dom)

    @bridge.bridge_command()
    async def finder(self, ctx: bridge.BridgeContext, acc):
        """Finds the list of the user's public social media accounts"""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        if acc == None:
            await send('**No account name entered**')
        else:
            ace = discord.Embed(title=acc, description="All the Found Links", color=discord.Colour.blurple())
            insta = urlify(acc)
            ace.add_field(name='Instagram:', value=f'[Instagram Profile](https://www.instagram.com/{insta}/?hl=en)', inline=False)
            ace.add_field(name=f'Github:', value=f'[Github Profile](https://github.com/{acc})', inline=False)
            ace.add_field(name=f'Twitter:', value=f'[Twitter Profile](https://twitter.com/{acc})', inline=False)
            ace.add_field(name=f'Reddit:', value=f'[Reddit Profile](https://reddit.com/u/{acc})', inline=False)
            ace.add_field(name=f'Twitch:', value=f'[Twitch Channel](https://twitch.tv/{acc})', inline=False)
            ace.set_thumbnail(url='https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356')
            await send(embed=ace)

    @bridge.bridge_command()
    async def checkemail(self, ctx, email):
        """Checks if the email is valid"""
        try:
            send = ctx.respond
        except:
            send = ctx.reply
        if email == '':
            await send('**No email entered**')
        else:
            try:
                val = check(email)
                if val == True:
                    dom = email.split('@')[1]
                    em = discord.Embed(title=f"Email Info", color=discord.Colour.blurple())
                    em.add_field(name="Email", value=f"`{email}`", inline=False)
                    em.add_field(name="Valid Format", value=f"`True`", inline=False)
                    em.add_field(name="Domain", value=f"`{dom}`", inline=False)
                    em.set_thumbnail(url=f'https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356')
                    await send(embed=em)
                else:
                    em = discord.Embed(title=f"Email Info", description="Invalid Email", color=discord.Colour.blurple())
                    em.set_thumbnail(url=f'https://images-ext-1.discordapp.net/external/gB4yj0jFMz0c0yHmHTihGRawp_kP65SpLhEbZg5s0So/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/d56b2bc1efe33b27fbc868c7fad87490.png?width=356&height=356')
                    await send(embed=em)
            except:
                await ctx.respond('404')
def setup(bot):
  bot.add_cog(info(bot))