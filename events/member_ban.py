import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class member_ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        e = discord.Embed(title=f":man_police_officer: :lock: **{user.mention} was banned**", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
        e.set_author(name=f"{user}", icon_url=f"{user.avatar.url}")
        channel = self.client.get_channel(int(self.log_channel))
        await channel.send(embed=e)

def setup(client):
    client.add_cog(member_ban(client))