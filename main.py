import discord
from discord.ext import commands
import os
import json

with open('db/database.json', 'r') as f:
    config = json.load(f)

AUTH = config['AUTH']

intents = discord.Intents.all()

intents.message_content = True

bot = commands.Bot(command_prefix='a!', intents=intents)
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
    await bot.change_presence(status=discord.Status.streaming, activity=discord.Streaming(name='a!help | Made For Educational Purposes', url='https://www.youtube.com/watch?v=1XzY2ij_vL4'))

bot.run(AUTH)