import discord
from discord.ext import commands

from cogs.dayz.bin.battlemetrics import DayZ

class dayz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("dayz online")

    @commands.command()
    async def dayz(self, ctx):
        server = 'la5540'
        z = DayZ(server=server)
        await ctx.send(f"```{server} | player_count: [{z.get_player_count()}]```")
    
async def setup(bot):
    await bot.add_cog(dayz(bot))