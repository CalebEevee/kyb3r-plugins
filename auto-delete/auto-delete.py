import discord
from discord.ext import commands


class ClaimPlugin(commands.Cog):
    """Advertisement Autodeleter"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channels = [
            976487777426358312, #level-2
            976487800381792256, #level-5
            976487821554630656, #level-10
            973909642931486740, #vip
            609737652958134282, #unlimited
            601581090938814476, #community
            601581967980494849, #gaming
            601590938560757761 #anime
        ]
