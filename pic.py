import discord
from discord.ext import commands

class Pic:
  def __init__(self, bot):
    self.bot = bot
    
    
  async def on_message(self, message):
    if message.author == self.bot.user:
      return
    if message.author.bot: return
    
    if message.content.startswith('embed'):
      await self.bot.send_message(message.channel, 'it is not set')
      
    if ('god') in message.content:
      embed = discord.Embed(title = 'EMINƎM', description = '', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://www.gannett-cdn.com/presto/2018/09/06/PDTF/c9571445-4fc8-4156-8562-dd11d01e6b4a-Detroit_rapper_Eminem-13.JPG?width=534&height=712&fit=bounds&auto=webp')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('meme'):
      embed = discord.Embed(title = 'BIGSMOKE', description = '', colour = discord.Colour.purple())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://vignette.wikia.nocookie.net/gta-myths/images/5/5a/Big_Smoke_SA.png/revision/latest?cb=20160817115555')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('Prisa'):
      embed = discord.Embed(title = 'Prisa', description = 'Owner of Chicken Server', colour = discord.Colour.orange())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://cdn.discordapp.com/attachments/455034541757693952/517751186242273281/t_bot_painted_good.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('Owner'):
      embed = discord.Embed(title = '', description = 'Chicken Server owner is <@381887710308335618>', colour = discord.Colour.orange())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://cdn.discordapp.com/attachments/455034541757693952/517751186242273281/t_bot_painted_good.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('Lord'):
      embed = discord.Embed(title = '', description = 'Lord Tachanka', colour = discord.Colour.green())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://i.kym-cdn.com/entries/icons/original/000/021/395/axi3q4APr3tkfnWkdiQPo7.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('venom'):
      embed = discord.Embed(title = '', description = 'Venom', colour = discord.Colour.dark_red())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://i.ytimg.com/vi/acNWDwnelLE/maxresdefault.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('MACHINE GUN KELLY'):
      embed = discord.Embed(title = '', description = '', colour = discord.Colour.blue())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://cdn.discordapp.com/attachments/459741965055950849/520667139007578140/download.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('hacker'):
      embed = discord.Embed(title = '', description = '', colour = discord.Colour.ping())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://cdn.discordapp.com/attachments/459741965055950849/520667139007578140/download.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if message.content.startswith('Oh'):
      embed = discord.Embed(title = 'Ohh', description = '', colour = discord.Colour.purple())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://i.imgur.com/xgz9nkR.gif')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if ('Spiderman') in message.content:
      embed = discord.Embed(title = 'Spiderman', description = '', colour = discord.Colour.red())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://www.jrc.cz/userfiles/Spidey1.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
    if ('KILLER') in message.content:
      embed = discord.Embed(title = 'Hitman', description = '', colour = discord.Colour.dark_red())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://cdn.discordapp.com/attachments/459741965055950849/520683912905883670/images_2.jpg')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
      if ('allahu akbar') in message.content:
      embed = discord.Embed(title = 'BOOOM', description = '', colour = discord.Colour.dark_red())
      embed.set_footer(text='')
      embed.set_thumbnail(url='')
      embed.set_image(url='https://media.giphy.com/media/cAhGEN7rmWWDH2H7kx/giphy.gif')
      embed.set_author(name='', icon_url='')
      await self.bot.send_message(message.channel, embed=embed)
      
  @commands.command()
  async def testall(self):
    await self.bot.say('lol')
    
def setup(bot):
  bot.add_cog(Pic(bot))
