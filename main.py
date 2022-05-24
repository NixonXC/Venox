import discord
from discord.ext import commands
import random
import os
import sys
import json
import datetime
import requests
import aiohttp
import time
import re
import whois

with open('db/database.json', 'r') as f:
    config = json.load(f)

AUTH = config['AUTH']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='a!', intents=intents)
bot.remove_command('help')

def urlify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '-', s)
    return s

@bot.command()
async def help(ctx):
    await ctx.send('`Available commands:`')
    em = discord.Embed(title='Available commands:', description='**List of all the commands | prefix: `a!`**', color=discord.Colour.blurple())
    em.add_field(name='`help`', value='Returns this message.', inline=False)
    em.add_field(name='`ping`', value='Returns the bot\'s latency.', inline=False)
    em.add_field(name='`finder <name>`', value='Finds accounts for the given account name.', inline=False)
    em.add_field(name='`ipwhois <ip>`', value='Returns information about the given IP address.', inline=False)
    em.add_field(name='`whois <domain>`', value='Returns the public info for the given domain.', inline=False)
    em.add_field(name="`instagram <name>`", value="Returns the instagram profile for the given user and tag.", inline=False)
    em.set_footer(text="This Bot is Made by NixonXC for educational purposes")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/717087150109879072/717087150109879072.png")
    await ctx.send(embed=em)

@bot.command()
async def finder(ctx, acc):
    if acc == '':
        await ctx.send('No account name entered')
    else:
        await ctx.send('`Searching...`')
        time.sleep(3)
        await ctx.send('`Code: 200 Found!`')
        time.sleep(1)
        ace = discord.Embed(title=acc, description="All the Found Links", color=0x00ff00)
        insta = urlify(acc)
        ace.add_field(name='Instagram:', value=f'[Instagram Profile](https://www.instagram.com/{insta}/?hl=en)', inline=False)
        ace.add_field(name=f'Github:', value=f'[Github Profile](https://github.com/{acc})', inline=False)
        ace.add_field(name=f'Twitter:', value=f'[Twitter Profile](https://twitter.com/{acc})', inline=False)
        ace.add_field(name=f'Reddit:', value=f'[Reddit Profile](https://reddit.com/u/{acc})', inline=False)
        ace.add_field(name=f'Twitch:', value=f'[Twitch Channel](https://twitch.tv/{acc})', inline=False)
        ace.set_thumbnail(url=f'https://images-ext-2.discordapp.net/external/1bEj6XyME-7647lmn13ldXvaCHYS07JozqwrFe8dSfQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/974012262442483752/814a40651600e969746cb62053bb0068.png?width=325&height=325')
        await ctx.send(embed=ace)
        await ctx.send('`Complete!`')

@bot.command()
async def whois(ctx, domain):
    import whois
    w = whois.whois(domain)
    await ctx.send(f"**DOMAIN:** `{domain}`")
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
    print(w)
    await ctx.send(embed=dom)

@bot.command()
async def ping(ctx):
    await ctx.send(f'`{0}`'.format(bot.latency))

async def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

@bot.command()
async def ipwhois(ctx, ip):
    if ip == "127.0.0.1":
        await ctx.send("Sorry, but I can't look up localhost")
        return
    if ip == None:
        await ctx.send("No IP entered, correct usage: `a!ipwhois <ip>`")
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
        await ctx.send(embed=em)

@ipwhois.error
async def ipwhois_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**No ip entered, correct usage: `a!ipwhois <ip>`**')

# make a instagram info command
@bot.command()
async def instagram(ctx, user):
    if user == None:
        await ctx.send('**No user entered, correct usage: `a!instagram <user>`**')
        return
    else:
        url = f"https://www.instagram.com/{user}/channel/?__a=1"
        headers = {'User-Agent': 'Mozilla'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.json()
        try:
            name = (f"`{data['graphql']['user']['full_name']}`")
        except:
            name = (f"`{data['graphql']['user']['username']}`")
        try:
            bio = (f"`{data['graphql']['user']['biography']}`")
        except:
            bio = (f"`No Bio`")
        try:
            followers = (f"`{data['graphql']['user']['edge_followed_by']['count']}`")
        except:
            followers = (f"`None`")
        try:
            following = (f"`{data['graphql']['user']['edge_follow']['count']}`")
        except:
            following = (f"`None`")
        embed = discord.Embed(title=name, description=bio, color=0x00ff00)
        embed.add_field(name="Followers", value=followers, inline=True)
        embed.add_field(name="Following", value=following, inline=True)
        await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print('Bot is ready!')
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print('------')
    await bot.change_presence(status=discord.Status.streaming, activity=discord.Streaming(name='a!help | Made For Educational Purposes', url='https://www.youtube.com/watch?v=1XzY2ij_vL4'))

bot.run(AUTH)