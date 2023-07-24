import discord
from discord.ext import tasks, commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=commands.DefaultHelpCommand())

async def load():
    for foldername in os.listdir('./cogs'):
        for filename in os.listdir(f'./cogs/{foldername}'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{foldername}.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())