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

with open('db/watchlist.json', 'r+') as f:
    onspo = json.load(f)

AUTH = config['AUTH']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='a!', intents=intents)
bot.remove_command('help')

def urlify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '-', s)
    return s

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

@bot.command()
async def help(ctx):
    await ctx.send('`Available commands:`')
    em = discord.Embed(title='Available commands:', description='`a!finder <account name>` - Finds accounts for the given account name.', color=discord.Colour.red())
    em.add_field(name='`a!ping`', value='Returns the bot\'s latency.', inline=False)
    em.add_field(name='`a!help`', value='Returns this message.', inline=False)
    em.add_field(name='`a!whois <domain>`', value='Returns the public info for the given domain.', inline=False)
    em.add_field(name='`a!tag <tag>`', value='Returns the tag\'s info.', inline=False)
    em.add_field(name='`a!tags`', value='Returns a list of all the tags.', inline=False)
    em.add_field(name='`a!taginfo`', value='Returns the info for the tag you are searched for.', inline=False)
    em.add_field(name='`a!addtag <tag>`', value='Adds a tag to the database.', inline=False)
    em.add_field(name='`a!deltag <tag>`', value='Removes a tag from the database.', inline=False)
    em.add_field(name='`a!tagaddinfo <tag> <info>`', value='Adds information about an tag to the database.', inline=False)
    em.add_field(name='`a!deltaginfo <tag>`', value='Delete information about an tag from the database.', inline=False)
    em.set_footer(text="This Bot is Made by NixonXC for educational purposes")
    await ctx.send(embed=em)

@bot.command()
@discord.is_owner()
async def tag(ctx, tag):
    if tag == '':
        await ctx.send('No tag entered')
    else:
        msg = await ctx.send('`Searching...`')
        time.sleep(3)
        if tag == '1':
            await msg.edit(f"`{onspo['1']}`")
        elif tag == '2':
            await msg.edit(f"`{onspo['2']}`")
        elif tag == '3':
            await msg.edit(f"`{onspo['3']}`")
        elif tag == '4':
            await msg.edit(f"`{onspo['4']}`")
        elif tag == '5':
            await msg.edit(f"`{onspo['5']}`")
        elif tag == '6':
            await msg.edit(f"`{onspo['6']}`")
        elif tag == '7':
            await msg.edit(f"`{onspo['7']}`")
        elif tag == '8':
            await msg.edit(f"`{onspo['8']}`")
        elif tag == '9':
            await msg.edit(f"`{onspo['9']}`")

@bot.command()
@discord.is_owner()
async def taginfo(ctx, tag):
    filename = 'db/infobase.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    if tag == None:
        await ctx.send('No tag entered')
    else:
        msg = await ctx.send('`Searching...`')
        time.sleep(3)
        if tag == '1':
            await msg.edit(f"{data['1']}")
        elif tag == '2':
            await msg.edit(f"{data['2']}")
        elif tag == '3':
            await msg.edit(f"{data['3']}")
        elif tag == '4':
            await msg.edit(f"{data['4']}")
        elif tag == '5':
            await msg.edit(f"{data['5']}")
        elif tag == '6':
            await msg.edit(f"{data['6']}")
        elif tag == '7':
            await msg.edit(f"{data['7']}")
        elif tag == '8':
            await msg.edit(f"{data['8']}")
        elif tag == '9':
            await msg.edit(f"{data['9']}")
        elif tag not in data:
            await msg.edit(f"`{tag}` is not a valid tag.")


@bot.command()
@discord.is_owner()
async def tags(ctx):
    await ctx.send('`Available tags:`')
    em = discord.Embed(title='Available tags:', description='`1`, `2` , `3`, `4`, `5`, `6`, `7`, `8`, `9`', color=discord.Colour.red())
    await ctx.send(embed=em)

@bot.command()
@discord.is_owner()
async def addtag(ctx, tag, name):
    filename = 'db/watchlist.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    if tag in data:
        await ctx.send('Tag already exists')
        return
    if name in data:
        await ctx.send('Name already exists')
        return
    if tag == None:
        await ctx.send('No tag entered, correct usage: `a!addtag <tag> <name>`')
        return
    if name == None:
        await ctx.send('No name entered, correct usage: `a!addtag <tag> <name>`')
        return
    else:
        filename = 'db/watchlist.json'
        with open(filename, 'r') as f:
            data = json.load(f)
        data[tag] = name
        await ctx.send(f'Tag `{tag}` added with name `{name}`')
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Created Tag: {tag} : {name}")

@bot.command()
@discord.is_owner()
async def addtaginfo(ctx, tag, info: str):
    filename = 'db/infobase.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    if tag in data:
        await ctx.send('Tag already exists')
        return
    if info == None:
        await ctx.send('No info entered, correct usage: `a!addtaginfo <tag> <info>`')
        return
    if tag == None:
        await ctx.send('No tag entered, correct usage: `a!addtaginfo <tag> <info>`')
        return
    else:
        filename = 'db/infobase.json'
        with open(filename, 'r') as f:
            data = json.load(f)
        data[tag] = info
        await ctx.send(f'Info for tag `{tag}` added')
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Created Info: `{tag}` : **{info}**")

@addtaginfo.error
async def addtaginfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('No tag or name entered, correct usage: `a!addtaginfo <tag> <info>`')
    if isinstance(error, commands.NotOwner):
        await ctx.send('You are not the owner of this bot')

@bot.command()
@discord.is_owner()
async def deltaginfo(ctx, tag):
    if tag == None:
        await ctx.send('No tag entered, correct usage: `a!deltag <tag>`')
        return
    else:
        filename = 'db/infobase.json'
        with open(filename, 'r') as f:
            data = json.load(f)
        del data[tag]
        await ctx.send(f'Tag `{tag}` deleted')
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Deleted tag " + tag)


@deltaginfo.error
async def deltaginfo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('No tag entered, correct usage: `a!deltaginfo <tag>`')
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Tag does not exist')
    if isinstance(error, commands.NotOwner):
        await ctx.send('You are not the owner of this bot')

@addtag.error
async def addtag_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('No tag or name entered, correct usage: `a!addtag <tag> <name>`')
    if isinstance(error, commands.NotOwner):
        await ctx.send('You are not the owner of this bot')

@bot.command()
@discord.is_owner()
async def deltag(ctx, tag):
    if tag == None:
        await ctx.send('No tag entered, correct usage: `a!deltag <tag>`')
        return
    else:
        filename = 'db/watchlist.json'
        with open(filename, 'r') as f:
            data = json.load(f)
        del data[tag]
        await ctx.send(f'Tag `{tag}` deleted')
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Deleted tag " + tag)

@deltag.error
async def deltag_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('No tag entered, correct usage: `a!deltag <tag>`')
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Tag does not exist')
    if isinstance(error, commands.NotOwner):
        await ctx.send('You are not the owner of this bot')

# make a instagram info command
@bot.command()
async def instagram(ctx, user):
    if user == None:
        await ctx.send('No user entered, correct usage: `a!instagram <user>`')
        return
    else:
        url = f"https://www.instagram.com/{user}/channel/?__a=1"
        headers = {'User-Agent': 'Mozilla'}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, header=headers) as r:
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