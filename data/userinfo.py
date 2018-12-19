import discord
from discord.ext import commands

class Userinfo:
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def userinfo(self, ctx, user: discord.User=None):
    if not user:
      user = ctx.message.author
    embed=discord.Embed(title=" ", description="{}".format(user.name), color=0xfed83d)
    embed.set_author(name=" ")
    embed.set_image(url=user.avatar_url)
    embed.add_field(name="Highest role", value=" {} ".format(user.top_role.mention), inline=True)
    if "508605450770448384" in(role.id for roles in user.role):
      await embed.add_filed(neme="Tier", value=" <@&508605450770448384> test", inline=True) 
    await self.bot.send_message(ctx.message.channel, embed=embed)
    
    
def setup(bot):
  bot.add_cog(Userinfo(bot))
