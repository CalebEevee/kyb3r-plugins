import discord
from discord.ext import commands


class AutoDelete(commands.Cog):
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
            601590938560757761, #anime
            696807165603610654, #over-100
            601631986863439872, #under-100
            602190781431676939, #kid friendly
            601586982576979978, #multi focus
            685958911328649231, #business
            601845293033455624, #roleplay
            601585067252383823, #fandom
            601582258385584138, #mental health
            619883127329914891, #tech-bot
            974324076657115206, #no description
            601580256939212840, #social media
            601806462460624896, #other websites
            601806623165644807, #youtube-twitch
            601833640594505749, #creative works
            701468749680607353, #discord bots
            601580532085817373, #search-partners
            601580517179260929, #search-staff
            617212714850189321 #search-work
        ]
        
        def check(m):
            return m.author == member

        logchannel = self.bot.get_channel(683072494013644817)

        for channel_id in channels:
            channel = await self.bot.get_channel(channel_id)
            deleted = await channel.purge(limit=100, check=check)

        embed = disnake.Embed(
            title="AutoDelete - Member Left",
            description=f"{member.name} `[ {member.id} ]` left. {len(deleted)} message(s) deleted!",
            color=0x56C9F0,
        )

        await logchannel.send(embed=embed)
        
        def setup(bot):
            bot.add_cog(AutoDelete(bot))
