import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("ping online")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("u gay")
    
async def setup(bot):
    await bot.add_cog(ping(bot))