import discord
from discord.ext import commands
import os
import json

with open('db/database.json', 'r') as f:
    config = json.load(f)

AUTH = config['AUTH']
PREFIX = config['PREFIX']
STREAM = config['STREAM_URL']
AUTHOR = config['AUTHOR']

intents = discord.Intents.all()

intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command('help')

async def loop():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{file[:-3]}") 
                print(f"[INFO] SUCCESSFULLY LOADED {file[:-3]} cog!")
            except Exception as e:
                print(f"[ERROR] {file[:-3]} LOADING FAILED!... Here's the error \n {e.__class__.__name__}: {e}")
bot.loop.create_task(loop())

@bot.event
async def on_ready():
    print('Bot is ready!')
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')
    print('------')
    await bot.change_presence(activity=discord.Streaming(name=f"{PREFIX}help | By {AUTHOR}, Made For Educational Purposes", url=STREAM))

bot.run(AUTH)